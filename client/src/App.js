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
    <div className = "container">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"></link>
      <h1>Basic Catan Board Generator</h1>
      <button type="button" class="btn btn-primary"onClick={generateBoard}>Shuffle</button>
      <Board fields={data}/>
    </div>

  )
}

export default App