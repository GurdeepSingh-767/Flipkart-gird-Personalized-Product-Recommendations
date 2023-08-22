import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { toast } from "react-toastify";

const MyModal = ({ visible, onClose }) => {

    const [user_name, setUser_name] = useState('');
    const [password, setPassword] = useState('');
    const [jwtToken, setJwtToken] = useState('');
    const navigate = useNavigate();
    // useEffect(() =>{
    //     if (localStorage.getItem('user-info')) {
    //         navigate("/")
    //     }
    // }, [])

    if (!visible) return null;


    const login = (e) => {
        e.preventDefault();
        if (validate()) {
            ///implentation
            // console.log('proceed');
            let inputobj={"user_name": user_name,
            "password": password};
            fetch("http://127.0.0.1:8000/api/login/",{
                method:'POST',
                headers:{'content-type':'application/json'},
                body:JSON.stringify(inputobj)
            }).then((res) => {
                return res.json();
            }).then((resp) => {
                console.log(resp)
                if (Object.keys(resp).length === 0) {
                    alert('Login failed, invalid credentials');
                }else{
                     toast.success('Success');
                     sessionStorage.setItem('user_name',user_name);
                     setJwtToken(resp.jwtToken);
                   navigate('/main',{ state: {user_name} })
                   
                }
                // if (Object.keys(resp).length === 0) {
                //     toast.error('Please Enter valid username');
                // } else {
                //     if (resp.password === password) {
                //         toast.success('Success');
                //         sessionStorage.setItem('username',username);
                //         usenavigate('/')
                //     }else{
                //         toast.error('Please Enter valid credentials');
                //     }
                // }
            }).catch((err) => {
                toast.error('Login Failed due to :' + err.message);
            });
        }
    }
    const validate = () => {
        let result = true;
        if (user_name === '' || user_name === null) {
            result = false;
            toast.warning('Please Enter Username');
        }
        if (password === '' || password === null) {
            result = false;
            toast.warning('Please Enter Password');
        }
        return result;
    }
    return (
        <div className="fixed inset-0 bg-black bg-opacity-30 backdrop-blur-sm flex flex-wrap justify-center items-center " >
            
            <div className="container  mx-auto  lg:w-2/6 md:w-1/2 bg-gray-200 rounded-lg p-8 flex flex-col md:ml-auto w-full mt-10 md:mt-0 relative">
            <button onClick={onClose} type="button" className=" absolute top-0 right-0 rounded-md p-3   text-gray-400 hover:text-black-700 "> <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg></button>
                <h1 className="text-gray-900 text-xl font-medium title-font mt-5 mb-5">LOGIN</h1>
                <form onSubmit={login} >
                    <div className="mb-2 leading-7 text-sm text-gray-600">
                        <label htmlFor="email">Email</label>
                        <input
                            type="text"
                            id="user_name"
                            className="form-control w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                            value={user_name}
                            onChange={(e) => setUser_name(e.target.value)}
                        />
                    </div>
                    <div className="mb-2 leading-7 text-sm text-gray-600 ">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            className="form-control w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                    <button type="submit" className="btn btn-primary text-white bg-pink-600 border-0 mt-3 mb-5 py-2 px-8 focus:outline-none hover:bg-pink-600 rounded  w-full text-lg">Login</button>
                </form>
            </div>

            

           
        </div>
    )
}

export default MyModal
