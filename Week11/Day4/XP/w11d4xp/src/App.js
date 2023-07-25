import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import ErrorBoundary from "./components/ErrorBoundary";
import React from "react"

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

export default class App extends React.Component{
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
}
