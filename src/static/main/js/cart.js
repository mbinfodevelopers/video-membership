// var updateBtns = document.getElementsByClassName('update-cart');
//
// for(var i = 0; i < updateBtns.length; i++){
//     updateBtns[i].addEventListener('click', function(){
//         var courseId = this.dataset.course
//         var action = this.dataset.action
//
//         if (user === 'AnonymousUser'){
//             console.log('Not logged in')
//         }else{
//             updateUserOrder(courseId, action)
//         }
//
//     })
// }
//
// function updateUserOrder(courseId, action){
//     console.log('logged in and sending data ...')
//     var url = '/order/update_item/'
//
//     fetch(url, {
//         method:'POST',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken
//         },
//         body:JSON.stringify({'courseId': courseId, 'action': action})
//     })
//         .then((response) =>{
//             return response.json()
//         })
//         .then((data) =>{
//             console.log('data', data)
//             location.reload()
//             })
// }

$('.addToCartBtn').click(function (e){
   e.preventDefault();

   var course_id = $('.cour_id').val();
   var token = $('input[name=csrfmiddlewaretoken]').val();
   console.log('token', token)
   $.ajax({
      method: "POST",
      url: "/order/add-to-cart/",
      data: {
         'course_id': course_id,
         csrfmiddlewaretoken: token
      },
      dataType: "",
      success: function (response) {
         console.log(response);
         // alertify.success(response.status)

      }
   })
      location.reload()
});

$('.delete-cart-item').click(function (e){
   e.preventDefault();

   var course_id = $('.course_id').val();
   var token = $('input[name=csrfmiddlewaretoken]').val();

   $.ajax({
      method: "POST",
      url: '/order/delete-cart-item',
      data: {
         'course_id': course_id,
         csrfmiddlewaretoken: token
      },
      success: function (response) {
         // alertify.success(response.status)
      }
   })
      location.reload()
});