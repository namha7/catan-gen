import React, { useState, useEffect } from 'react'
import Board from "./Board"


function App() {

  function generateBoard() {
    fetch("/fields").then(
      res => res.json()
    ).then(
      data => {
            setData(data)
            console.log(data)
      }
    )
  }

  const [data, setData] = useState([])
  useEffect(() => {
    fetch("/fields").then(
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
      <button onClick={generateBoard}>Shuffle</button>
      <Board fields={data}/>
      {(typeof data.fields === "undefined") ? (
        <p>Loading...</p>
      ) : ( 
        data.fields.map((fields, i) => (
          <p key={i}>{fields}</p>
        ))
      )}
    <pre>
    {JSON.stringify(data, null, 2)}
    </pre>
    </div>

  )
}

export default App