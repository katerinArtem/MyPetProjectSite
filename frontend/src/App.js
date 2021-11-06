import React, {useState,useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from "./components/navigation/Navbar";
import Content from "./components/content/Content";
import Footer from "./components/footer/Footer";
import "./styles/App.css"

function App() {

  var  [posts,setPosts] = useState([])
  posts = posts
  useEffect(()=>{
    axios({
      method:"GET",
      url:"http://127.0.0.1:8000/api/posts/"
    }).then(response =>{
      setPosts(response.data)
    })
  },[])

  return (
    <div className="App">
      <div className="wrapper">
          <Navbar/>
          <Content/>
          <Footer/>
      </div>  
    </div>
  );
}

export default App;
