import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import ErrorBoundary from "./components/ErrorBoundary";
import React from "react"
import PostList from "./components/PostList";

const Home = () => {
  return <h1>Home</h1>
}

const Profile = () => {
  return <h1>Profile</h1>
}

const Shop = () => {
  throw new Error ("an error has occured")
}

const routes = (
    <Routes>
    <Route exact path="/" element={<Home />} />
    <Route path="/profile" element={<Profile />} />
    <Route  path="/shop" element={<Shop />} />
  </Routes>
  
)

function Navbar() {
  return (
    <>
        <p>
        <NavLink to="/">Home</NavLink>

        </p>
        <p>
        <NavLink to="/profile">Profile</NavLink>

        </p>
        <p>
        <NavLink to="/shop">Shop</NavLink>

        </p>

     </>
  )
}

class App extends React.Component{
  render() {
  return (
    <ErrorBoundary>
      <BrowserRouter>
      <Navbar />
      <ErrorBoundary>
        {routes}
      </ErrorBoundary>
      </BrowserRouter>
    </ErrorBoundary>
  );
}
};

const XP2 = (props) => {
  return(
    <PostList />
  )
};

const handleClick = async (props) =>{
  try {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        key1: 'myusername',
        email: 'mymail@gmail.com',
        name: 'Isaac',
        lastname: 'Doe',
        age: 27
      })
    };
    const response = await fetch("https://webhook.site/fc108802-57d0-4232-86f5-c76bf14c0493", options);
    console.log(response)
  } catch (error){
    console.log(error)
  }
  
}
const XP4 = (props) => {
  return(
    <button onClick={handleClick}>Post Data</button>
  )
}

export default XP4