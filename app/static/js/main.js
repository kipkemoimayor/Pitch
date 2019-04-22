$(document).ready(function () {
  $("#update").click(function(){
    Swal.fire({
    type: 'success',
    title: 'Success',
    text: 'Profile Updated ',
    timer:2000,
    showConfirmButton:false
  })
  })

  $(".title").mouseover(function(){
    $("span").show()

  })
  $("#login").click(function(){
    Swal.fire({
    type: 'warning',
    title: 'Login Required',
    text: 'Please Login to Post your Idea',
    html:'<a class="btn default-color" href="/authenticate/login">Sign in</a>',
    showConfirmButton:false
  })
  })

})
