
import React, { useState, useEffect} from "react";
import { useNavigate } from 'react-router-dom';

import "./login.css";
import dogImage from "./img/dog.png";



function Login(){

    const navigate = useNavigate();

    //API
    let [userList, setUserList] = useState([])

    useEffect(() => {
        getUserList()
    }, [])

    let getUserList = async () => {
        let response = await fetch('/api/users/')
        let data = await response.json()
        console.log('data', data)
        
        setUserList(data)
    }


    //call to backend
    let updateUser = async (user) => {
        fetch(`/api/users/${user['id']}/update/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        })         
    }

    

    let onSignIn = () => {
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        const matchingUsers = userList.filter(user => user.username === email && user.password === password);
        
        if (matchingUsers.length > 0) {
            const user = matchingUsers[0];
            console.log(user, user.id, user.username, email, password);
            user.isCurrentUser = true;
            
            updateUser(user);
            navigate('/profile');

        } else {
            console.log("Users not found or incorrect password.");
        }
    }

    return(
        <div className="loginbody">
            <main className="loginmain">
                
                <div style={{width: "50%", height:'100vh', minHeight:"800px", overflow:"hidden"}}>
                    <img className="loginimg" src={dogImage} alt="Happy Doggie" style={{ height: '100%', width: '100%', objectFit:"cover"}} />
                </div>
                

                <section className="logincontent">
                    <a href={`/`} style={{marginLeft: 'auto'}}>
                        <i className="fa-solid fa-x fa-xl" style={{color: 'rgb(182, 106, 29)' }}></i>
                    </a>
                    <h1>Sign in</h1>
                    <hr className="loginHr"/>
                    <div className="loginlogo">
                        <a href="www.facebook.com/jameelmarco.ursonal">
                            <i className="fa-brands fa-facebook fa-sm" style={{color: '#cc8033' }}></i>
                        </a>
                        <a href="www.facebook.com/jameelmarco.ursonal">
                            <i className="fa-brands fa-google fa-sm" style={{color: '#cc8033' }}></i>
                        </a>
                        <a href="www.facebook.com/jameelmarco.ursonal">
                            <i className="fa-brands fa-twitter fa-sm" style={{color: '#cc8033' }}></i>
                        </a>
                    </div>
                    <p className="loginsignin">Or Sign in To Continue</p>
                    <div className="loginform">
                        <input id="email" name="email" type="text" placeholder="Username" required/>
                        <input id="password" name="password" type="password" placeholder="Password" required/>
                        <div className="loginremember">
                            <div className="left">
                                <input type="checkbox" />
                                <p>Remember Me</p>
                            </div>
                            <div className="right">
                                <a href="www.facebook.com/jeb.bajenting">
                                    <span>Forgot Password?</span>
                                </a>
                            </div>
                        </div>
                        <div className="login_button">
                            <button onClick={onSignIn}>Sign In</button>
                        </div>
                    </div>
                    
                    <div className="signupterms">
                        <span>Don't have an Account?</span>
                        &nbsp;
                        <a href={`/signup`}>
                            <span><b>Sign Up</b></span>
                        </a>
                    </div>
                    <div className="loginterms">
                        <a href="www.facebook.com/jameelmarco.ursonal">
                            <span><b>Terms & Conditions</b></span>
                        </a>
                        
                        <a href="www.facebook.com/jameelmarco.ursonal">
                            <span><b>Privacy Policy</b></span>
                        </a>
                    </div>
                </section>
            </main>
        </div>
    )
}

export default Login;