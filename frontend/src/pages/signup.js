

import { useNavigate } from 'react-router-dom';

import "./login.css"
import "./signup.css"
import catImage from "./img/cat.png"

function Signup(){

    const navigate = useNavigate();

    let createUser = async (user) => {
        fetch(`/api/users/create/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        })       
    }


    const handleOnSignUp = () => {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        console.log(username, password, confirmPassword);

        if(password===confirmPassword){
            const user = {
                username: username,
                password: password,

            };
            createUser(user);
            navigate('/login');
        }
        else{
            alert("Passwords don't match");
        }
    }


    return(
        <div className="loginbody">
            <main className="signupmain">
                
                <div className='bg-dark-brown flex items-center w-1/2 h-screen min-h-[800px] overflow-hidden'>
                    <img src={catImage} alt="Fierce El Gato" className="h-4/5"/>
                </div>
                
                <section className="signupcontent">
                    <a href={`/`} style={{marginLeft: 'auto'}}>
                        <i className="fa-solid fa-x fa-xl" style={{color: 'rgb(182, 106, 29)' }}></i>
                    </a>
                    <h1>Sign Up</h1>
                    <hr className="signupHr"/>
                    <div className="loginform" action="">
                        <input type="text" id="username" placeholder="Username" />
                        <input type="email" id="email" placeholder="Email" />
                        <input type="password" id="password" placeholder="Password" />
                        <input type="password" id="confirmPassword" placeholder="Confirm Password" />
                        
                        <div className="signup_button">
                            <button onClick={handleOnSignUp}>Sign Up</button>
                        </div>
                    </div>
                    <div className="signupterms">
                       
                            <span>Already Have Account?</span>
                       
                        &nbsp;
                        <a href={`/login`}>
                            <span><b>Sign in</b></span>
                        </a>
                    </div>
                </section>
            </main>
        </div>
    )
}


export default Signup;















 //API
    // let [userList, setUserList] = useState([])

    // useEffect(() => {
    //     getUserList()
    // }, [])

    // let getUserList = async () => {
    //     let response = await fetch('/api/users/')
    //     let data = await response.json()
    //     console.log('data', data)
        
    //     setUserList(data)
    // }
