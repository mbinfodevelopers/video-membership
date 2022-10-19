from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from course.models import Course
from .models import Account
from .forms import AccountAuthenticationForm, RegistrationForm, AccountUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.conf import settings


def profile_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get('user_id')
    try:
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse('something went wrong.')
    context = {
        'user': request.user,
    }
    return render(request, 'account/profile.html', context)


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect('course:courses')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


@login_required(login_url='account:login')
def login_view(request, *args, **kwargs):
    # user = request.user
    # if user.is_authenticated:
    #     return redirect("course:courses")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=raw_password)
            if user:
                login(request, user)
                return redirect('course:courses')
    else:
        form = AccountAuthenticationForm()

    context = {
        "login_form": form
    }

    return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("course:courses")


@login_required(login_url='account:login')
def edit_account_view(request, *args, **kwargs):
    user_id = kwargs.get("user_id")
    account = Account.objects.get(pk=user_id)
    if account.pk != request.user.pk:
        return HttpResponse("You cannot edit someone elses profile.")
    context = {}
    if request.POST:
            form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                new_username = form.cleaned_data['username']
                return redirect("course:courses")
            else:
                form = AccountUpdateForm(request.POST, instance=request.user,
                    initial={
                        "id": account.pk,
                        "email": account.email,
                        "username": account.username,
                        "profile_image": account.profile_image,
                        "hide_email": account.hide_email,
                    }
                )
                context['form'] = form
    else:
        form = AccountUpdateForm(
            initial={
                    "id": account.pk,
                    "email": account.email,
                    "username": account.username,
                    "profile_image": account.profile_image,
                    "hide_email": account.hide_email,
                }
            )
    context['form'] = form
    context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    return render(request, "account/edit_account.html", context)


def free_courses(request):
    free_course = Course.objects.filter(is_free=True)
    context = {
        'free_course': free_course,
    }
    return render(request, 'account/free_course.html', context)


def money_courses(request):
    my_course = Course.objects.filter(status=True)
    context = {
        'my_course': my_course,
    }

    return render(request, 'account/myCourse.html', context)