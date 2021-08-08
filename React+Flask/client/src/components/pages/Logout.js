import React from 'react'
import { Link } from 'react-router-dom';
import {Button} from './Button';
import './FormSignup.css';
import $ from 'jquery'

function Logout(){
    $.ajax({
        url: "/logout",
        type: "GET",
     } );
    return (
    <div style={{alignSelf: 'center'}}><h1>You are logged out!</h1></div>
    )
}
export default Logout;