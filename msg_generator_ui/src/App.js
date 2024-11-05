import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';

function App() {
  //using state to create payload for api call
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });

  //to capture changes in the form-input
  const handleChange = (e)=>{
    const {name, value} = e.target;
    setFormData({...formData, [name]:value});
  }

  //call backend api using formData to generate personalised message
  const handleSubmit = async(e)=>{
    e.preventDefault();
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
          <div class = "col"> <input name="profileurl" class = "form-control text-center" placeholder = "Profile URL" value={FormData.password} onChange={handleChange}/></div>       
        </div>
        <div class = "col">
          <button type="submit" class="btn btn-success btn-md">Generate Message</button>
        </div>
        </form>
      </div>
    </div>
  );
}

export default App;
