(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {

    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("btnScroll").style.display = "block";
    } else {
        document.getElementById("btnScroll").style.display = "none";

    }


}

function toUp() {

    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;

}



// function redirection() {

//     let url = "signUp.html";
//     window.location.href(url);


// }


// function onLoading() {

//     let LoadingPage = dodocument.getElementsByClassName("loading");
//     LoadingPage.addEventListener('onload'),
//         function() {

//             console.log("you have finished your loading page");

//         }

// }


function Register() {

    let message;

    if (document.form.input.value == "email") {
        
        message = "thanks for registration!";
        input.preventDefault();
        input.stopPropagation();
    } else if (document.form.input.value == "exist") {

        message = "your are already exist";
        input.preventDefault();
        input.stopPropagation();

    }else {

        message = "not valid email! Please try again";
        input.preventDefault();
        input.stopPropagation();
    }

    document.getElementsByClassName("message").innerText = message;

}

