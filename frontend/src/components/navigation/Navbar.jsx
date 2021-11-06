import React, {useState,useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../../styles/navigation/Navbar.css'

const Navbar = () => {
  return (
      <div className="fixed-top _navbar" id="navMenu">
            <div className="itemlist" >
              <a className="linkItem" href="{% url 'main:home' %}"><div>Home</div></a>
              <a className="linkItem" href="{% url 'main:posts' %}"><div>Posts</div></a>
              <a className="linkItem" href="{% url 'main:features' %}"><div>Features</div></a>
              <form className="formItem">Input</form>
              <div className="_dropdown" >
                <button className="_dropbtn">Username</button>
                <div className="_dropdown-content" style={{right:0}}>
                  <a href="{% url 'main:profile_update' %}">Profile</a>
                  <a href="{% url 'main:profile_posts' %}">Your posts</a>
                  <a href="{% url 'main:profile_dialogs' %}">Dialogs</a>
                  <a href="{% url 'logout' %}">Logout</a>
                  <a href="{% url 'main:home'%}admin/">Admin Panel</a>
                </div>
              </div>
              <a className="imglinkItem" href="{% url 'main:profile_update' %}">
                Image
              </a>
              <button className="btn btn-outline-light" id="Login" type="button">Login</button>
              <button className="btn btn-warning " id="Sign-up" type="button">Sign-up</button>
            </div>
        </div>
  );
}

export default Navbar;
