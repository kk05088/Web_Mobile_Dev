import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Admin from './admin';
import Home from './home';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  //   const [isPending,startTransition] = useTransition();
  const handleSubmit = (event) => {
    event.preventDefault();
    if (username === 'admin' && password === 'password') {
      navigate('/Admin', { replace: true });
    } else {
      navigate('/home', { replace: true });
    }
  };

  
  return (
    <div>
      <h2>Login Page</h2>
      <form method="post" onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={(event) => setUsername(event.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
        </label>
        <br />
            <button type="submit"  >Submit</button>
      </form>
        
        
    </div>
  );
};

export default LoginPage;