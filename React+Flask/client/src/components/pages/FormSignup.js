import React from 'react'
import { Link } from 'react-router-dom';
import {Button} from './Button';
import './FormSignup.css';
import $ from 'jquery'

function get_values(){
    let username = document.querySelector('#usernameInput').value
    let email = document.querySelector('#emailInput').value
    let password = document.querySelector('#passwordInput').value

    console.log(password)
    $.ajax({
        url: "/testing",
        data: {
            username: username,
            email: email,
            password: password
        },
        dataType: "JSON",
        type: "POST",
        success: function(data){
         console.log(data)
      }
          }
        )
    ;

    // fetch('/test', {
    // method: 'POST', // or 'PUT'
    // headers: {
    //   'Content-Type': 'application/json',
    // },
    // body: JSON.stringify(data),
    // })
    // .then(response => response.json())
    // .then(data => {
    //   console.log('Success:', data);
    // })
    // .catch((error) => {
    //   console.error('Error:', error);
    // });
}

function FormSignup() {
  return (
    <div>
      <div className="form-content-right">
        <form className="form">
          <h1>Sign Up Here!</h1>
          <div className="form-inputs">
            <label htmlFor="username" className="form-label">
              Username
            </label>
            <input type="text" 
              className="form-input"
              placeholder="Enter your username"
              id = "usernameInput"
              />
          </div>
          <div className="form-inputs">
            <label className="form-label">
            Email
            </label>
            <input type="email" 
              className="form-input"
              placeholder="Enter your email"
              id = "emailInput"

              />
  
          </div>
          <div className="form-inputs">
            <label className="form-label">
            Password
            </label>
            <input type="password" 
              className="form-input"
              placeholder="Enter your password"
              id = "passwordInput"
              />
          </div>
          <Button className='form-input-btn' type="button" onClick={get_values} buttonSize='btn--medium' buttonColor='green'>
            Sign Up 
          </Button>
          <span className="form-input-login">
             Already have an account? Login <Link to='/sign-in'>
               here
             </Link>
             </span>
        </form>
      </div>
    </div>
  )
}

export default FormSignup
