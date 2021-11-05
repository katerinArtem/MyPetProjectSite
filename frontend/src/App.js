import React, {useState,useEffect} from 'react';
import './App.css';
import axios from 'axios';

function App() {

  var  [posts,setPosts] = useState([])

  useEffect(()=>{
    axios({
      method:"GET",
      url:"http://127.0.0.1:8000/api/posts/"
    }).then(response =>{
      setPosts(response.data)
      console.log(response.data)
    })
  },[])

  return (
    <div className="App">
      <h1>hello from react!!</h1>
      <div className="posts">
        <ul>{posts.map(p =>(
          <li key={p.date_created}>
            <div>{p.author}</div>
            <div>{p.title}</div>
            <div>{p.content}</div>
            <div>{p.date_created}</div>
            </li>
        ))}</ul>
      </div>    
    </div>
  );
}

export default App;
