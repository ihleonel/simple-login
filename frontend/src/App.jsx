import { useState } from "react"

export default function App() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const submit = () => {
    fetch('http://localhost:8000/login', {
      method: 'POST',
      body: JSON.stringify({username, password}),
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then(response => response.json)
    .then(data => console.log(data))
  }
  return (
    <>
      <h3>Login</h3>
      <label>Username</label>
      <input type="text"
        value={username}
        onChange={(event) => setUsername(event.target.value)}
      />
      <label>Password</label>
      <input type="password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
      />
      <button type="submit" onClick={() => submit()}>Submit</button>
    </>
  )
}
