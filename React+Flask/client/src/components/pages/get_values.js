
import $ from 'jquery'

function get_values(){
    let username = document.querySelector('#usernameInput').value
    let email = document.querySelector('#emailInput').value
    let password = document.querySelector('#passwordInput').value

    $.ajax({
        url: "/sign-up",
        data: {
            username: username,
            email: email,
            password: password
        },
        dataType: "JSON",
        type: "POST",
        }
    );
}

export default get_values