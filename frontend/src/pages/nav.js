import React, { useState, useEffect} from "react";
import { useNavigate } from "react-router-dom"

import "./landing.css"
import "./profile.css"
import logoImage from "./img/logo.png"


function Nav(){

    const [show, setShow] = useState(false);
    const navigate = useNavigate();


    //FOR GETTING USERS - START
    //getting the user list
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


    //getting the current user values
    const currentUser = userList.filter(user => user.isCurrentUser === true);
    const accessCurrentUser = currentUser[0];
    console.log(accessCurrentUser, 100*7)
    //FOR GETTING USERS - END



    //FOR LOGGIN OUT - START
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

    //when log out button clicked
    const handleOnLogOut = () => {
        accessCurrentUser.isCurrentUser = false;
        updateUser(accessCurrentUser);
        navigate('/login')
    }
    //FOR LOGGIN OUT - end



    //FOR DELETING ACCOUNT - START
    //when delete button is clicked
    const handleOnDelete = () => {
        deleteUser(accessCurrentUser);
        navigate('/')
    }

    //call to backend
    let deleteUser = async (user) => {
        fetch(`/api/users/${user['id']}/delete/`, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json'
            },
        })       
    }

    //FOR DELETING ACCOUNT - END
    



    return (
        <div>
            <nav className="landingnav">
                <div className="logo" onClick={() => {navigate('/home')}}>
                    <img src={logoImage} alt="PurrfectlyRated Logo" />
                    <h1>Purrfectly<span className="rated">Rated</span></h1>
                </div>
                <ul>
                    <li onClick={() => {navigate('/home')}}>Home</li>
                    <li>About Us</li>
                    <li>Collections</li>
                    <li>Gallery</li>
                </ul>
                <div className="icons">
                    <i className="fa fa-search transparent-icon"></i>
            
                    <button className="noStyle" onClick={() => {setShow(!show)}}>
                        <i className="fa fa-user transparent-icon"></i>
                    </button>
                </div>
            </nav>

            {show && <div className="settingsDiv">
                <div className="settingsSubDiv" onClick={() => {navigate('/profile')}}><i className="fa-solid fa-user"></i>Your Profile</div>
                <div className="settingsSubDiv" onClick={handleOnDelete}><i className="fa-solid fa-user"></i>Delete Account</div>
                <div className="settingsSubDiv" onClick={handleOnLogOut}><i className="fa-solid fa-right-from-bracket"></i>Log Out</div>
            </div>}
        </div>
    )
}

export default Nav;