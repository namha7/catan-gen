import React, { useState, useEffect } from 'react'
import Board from "./Board"

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
    <div>
      <h1>Basic Catan Board Generator</h1>
      <Board />
      {(typeof data.members === "undefined") ? (
        <p>Loading...</p>
      ) : ( 
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  )
}

export default App