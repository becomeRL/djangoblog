const login = document.querySelector('.js-login_content'),
    greeting = document.querySelector('.js-greeting');

$(greeting).fadeIn(2000);
$(greeting).fadeOut(2000);
setTimeout(function(){
    $(login).fadeIn(2000)
}, 4000)
