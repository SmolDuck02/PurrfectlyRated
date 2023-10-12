import React from 'react';
import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import ReactDOM from 'react-dom/client';

import Landing from './pages/landing'
import Login from './pages/login';
import Signup from './pages/signup';
import Profile from './pages/profile';
import Home from './pages/home';

import './index.css';

import ImageUploadForm from './pages/baba';
// import ProductList from "./pages/products"
// import { UserProvider } from './pages/UserContext';

const router = createBrowserRouter([
  
  {
    path: "/",
    element: <Landing/>,
  },
  {
    path: "/home",
    element: <Home />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/signup",
    element: <Signup />,
  },
  {
    path: "/profile",
    element: <Profile />,
  },
]);


const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(

  <React.StrictMode>
    
       <RouterProvider router={router} />
    
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();







/* <UserProvider>
       <RouterProvider router={router} />
</UserProvider> */