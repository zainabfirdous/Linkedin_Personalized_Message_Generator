import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import axios from 'axios'; 

function App() {
  //using state to create payload for api call
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    profileUrl: '',
  });

  const [message, setMessage] = useState('');

  const [user, setUser] = useState({
    name: '',
    location: '',
    posts: []
  })

  //to capture changes in the form-input
  const handleChange = (e)=>{
    const {name, value} = e.target;
    console.log(formData)
    setFormData({...formData, [name]:value});
  }

  //call backend api using formData to generate personalised message
  const handleSubmit = async(e)=>{
    e.preventDefault();
    const user_data = await axios.post('http://127.0.0.1:8000/', formData)
    setUser({
      name:user_data.data.details.name,
      location:user_data.data.details.location,
      posts:user_data.data.details.posts
    })
  }

  const generateMessage = async(e)=>{
    e.preventDefault()
    let result = await axios.get(`http://127.0.0.1:8000/generate?name=${user.name}`)
    console.log(result)
    setMessage(result.data[0])
  }

  return (
    <div className="App">
      <div class = "container text-center">
        <div class= "row">
          <p>Welcome! I am happy to craft a personalized linkedIn message for you.</p>
          <br/>
          <p>To proceed please provide the following details.</p></div>
        <form onSubmit={handleSubmit}>
        <div class = "row">
          <div class = "col"><label class = "form-label">LinkedIn Username</label></div>
          <div class = "col"><input name = "username" class = "form-control text-center" placeholder = "Username" value={FormData.username} onChange={handleChange}/></div>       
        </div>
        <div class = "row">
          <div class = "col"><label class = "form-label">LinkedIn Password</label></div>
          <div class = "col"> <input name="password" class = "form-control text-center" placeholder = "Password" value={FormData.password} onChange={handleChange}/></div>       
        </div>
        <div class = "row">
          <div class = "col"><label class = "form-label">Target Profile URL</label></div>
          <div class = "col"> <input name="profileUrl" class = "form-control text-center" placeholder = "Profile URL" value={FormData.profileUrl} onChange={handleChange}/></div>       
        </div>
        <div class = "col">
          <button type="submit" class="btn btn-success btn-md">Fetch Posts</button>
        </div>
        </form>
      </div>

      {user.posts.length>0 && message === '' && 
      <div class="container text-center">
      <button type='submit' class="btn btn-success btn-md" onClick={generateMessage}>Generate Message</button>
      <table class="table">
        <thead>
          <tr><th scope='col'>Posts</th></tr>
        </thead>
        <tbody>
          {user.posts.map((post,index)=>(
            <tr key={index}>
              <td>{post}</td>
            </tr>
          ))}
        </tbody>
      </table>
      </div> }

      {message.length>0 &&
      <div class="container text-center">
        {message}
      </div>}
    </div>
  );
}

export default App;
