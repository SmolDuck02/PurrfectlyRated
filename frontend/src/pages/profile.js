import React, { useState, useEffect} from "react";
import Nav from "./nav";

import "./profile.css"
import "./landing.css"
import defaultUserPFP from "./img/pfp.png"



function Profile(){
    
    //FOR GETTING USER - START
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


    //getting the current user
    const currentUser = userList.filter(user => user.isCurrentUser === true);
    const accessCurrentUser = currentUser[0];
    console.log(accessCurrentUser, 100*7)
    //FOR GETTING USER -END


    const handleScrollToCenter = () => {
        // Get the viewport height
        const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
    
        // Calculate the position to scroll to (center of the viewport)
        const scrollToPosition = viewportHeight / 2;
    
        // Scroll the page to the calculated position
        window.scrollTo({ top: scrollToPosition, behavior: "smooth" });
    };


    return (
        <div className="profilebody">

            <Nav />

            <div className="profileUserDetailsContainer">
                <div className="profileUserBackground">
                    <div className="profileUserPicture">
                        {/* <img src={defaultPFP} alt="user pfp"></img> */}
                    </div>
                </div>
                
                <div className="profileUserName">
                    {accessCurrentUser ? (
                        <h1>{accessCurrentUser.username[0].toUpperCase() + accessCurrentUser.username.slice(1)}</h1>
                    ) : ( <p></p>
                    )}
                    <button className="profileButton"><b><i className="fa-solid fa-pen fa-xs"></i>&emsp;Edit Profile</b></button>
                </div>
            </div>

            <div className="makeReviewContainer">
                <div className="top">
                    <img src={defaultUserPFP} className="profileMiniUserPicture" alt="mini user pfp"/>
                    <form action="">
                        <input onClick={handleScrollToCenter} type="text" id="review" name="review" placeholder="Search For A Product To Review &#9733;" required/>
                    </form>
                    <button className="pawButton"><i className="fa-solid fa-paw "></i> </button>
                </div>
                {/* <hr className="profileHr"/> */}
                
            </div>

            <div className="profileReviews">
                 <p>No Reviews Made.</p>
            </div>
        </div>
    )
}


export default Profile;