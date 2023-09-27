
import { useNavigate } from 'react-router-dom';

import "./landing.css"
import logoImage from "./img/logo.png"
import petImage from "./img/image.png"
import foodImage from "./img/food.png"
import bowlImage from "./img/bowl.png"
import boneImage from "./img/bone.png"
import cageImage from "./img/petcage.png"

function Landing(){

    const navigate = useNavigate();

    return (
        <div className="landingbody">
            <nav className="landingnav">
                <div className="logo">
                    <img src={logoImage} alt="PurrfectlyRated Logo"/>
                    <h1>Purrfectly<span className="rated">Rated</span></h1>
                </div>
                <ul>
                    <li onClick={() => {navigate('/login')}}>Home</li>
                    <li>About Us</li>
                    <li>Collections</li>
                    <li>Gallery</li>
                </ul>
                <div className="icons">
                    {/* <a href={`/signup`}>
                        <i className="fa fa-search transparent-icon"></i>
                    </a> */}
                    <a href={`/login/`} id="user-icon">
                        <i className="fa fa-user transparent-icon"></i>
                    </a>
                    {/* <a href={`https://www.facebook.com/jeb.bajenting`}>
                        <i className="fa fa-shopping-cart transparent-icon"></i>
                    </a> */}
                </div>
            </nav>


            <main>
                <section>
                    <div className="first">
                        <div className="intro">
                            <h1>Paws & Applause:</h1>
                            <h1>Elevating Pet Product</h1>
                            <h1>Experiences!</h1>
                            <span>Our go-to destination for insightful and comprehensive reviews</span>
                            <br />
                            <button className="signUpNowButton" onClick={() => {navigate('/signup')}}>Sign Up Now!</button>
                        </div>
                        <img src={petImage} alt="This is pets!"/>
                    </div>
                </section>

                <section className="second">
                    {/* <h1 className="pet--products">Pet Products</h1> */}
                    <div className="parent--container">
                        <div className="container">
                            <img src={cageImage} alt="This is petcage!"/>
                            <div className="description">
                                <div class="info">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <span>(124)</span>
                                    <i class="far fa-heart"></i>
                                </div>
                                {/* <h1>Pet Cage</h1> */}
                            </div>
                        </div>

                        <div class="container">
                            <img src={bowlImage} alt="This is pet bowl!"/>
                            <div class="description">
                                <div class="info">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="far fa-star"></i>
                                    <span>(200)</span>
                                    <i class="far fa-heart"></i>
                                </div>
                                {/* <h1>Bowl</h1> */}
                            </div>
                        </div>

                        <div className="container">
                            <img src={foodImage} alt="This is pet food!" />
                            <div className="description">
                                <div className="info">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <span>(604)</span>
                                    <i class="far fa-heart"></i>
                                </div>
                                {/* <h1>Food</h1> */}
                            </div>
                        </div>

                        <div className="container">
                            <img src={boneImage} alt="This is pet bone!"/>
                            <div className="description">
                                <div className="info">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="far fa-star"></i>
                                    <i class="far fa-star"></i>
                                    <span>(176)</span>
                                    <i class="far fa-heart"></i>
                                </div>
                                {/* <h1>Bone</h1> */}
                            </div>
                        </div>
                    </div>
                </section>
            </main>
        </div>
    )
}


export default Landing;