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
         // console.log('respose', response)

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