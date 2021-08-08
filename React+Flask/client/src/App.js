import { useState, useEffect } from "react";
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";
import './App.css'
import Navbar from "./components/pages/Navbar";
import Home from  "./components/pages/HomePage/Home";
import Prices from  "./components/pages/Prices-Trends/Prices";
import Wish from  "./components/pages/Wishlist/Wish";
import Form from  "./components/pages/FormSignup";
import Logout from "./components/pages/Logout";


function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <Router>
      <Navbar/>
      <Switch>
        <Route path='/' exact component={Home}/>
        <Route path='/sign-up' component={Form}/>
        <Route path='/prices' component={Prices}/>
        <Route path='/wishlist' component={Wish}/>
        <Route path='/logout' component={Logout}/>

      </Switch>
    </Router>
  )
  
}

export default App