from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import AccountAuthenticationForm, RegistrationForm, AccountUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.conf import settings
from django.core import files


def home_view(request):
    queryset = Account.objects.all()
    dic = {
        "queryset": queryset
    }
    return render(request, "home.html", dic)


def profile_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get('user_id')
    try:
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse('something went wrong.')
    context = {
        'user': request.user
    }
    return render(request, 'account/profile.html', context)


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticate as " + str(user.email))
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
            return redirect('account:home')

        else:
            form = RegistrationForm()
            context['registration_form'] = form

    return render(request, "account/register.html", context)


def login_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("account:home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=raw_password)

            if user:
                login(request,user)
                return redirect("account:home")

    else:
        form = AccountAuthenticationForm()

    context = {
        "login_form" : form
    }

    return render(request, "account/login.html", context)


def logout_view(request):
    print("LOGGING OUT")
    logout(request)
    return redirect("account:home")


def edit_account_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("account:login")
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
                return redirect("account:home")
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