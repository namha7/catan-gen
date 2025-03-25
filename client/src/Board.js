import React, { Component } from 'react';
import { HexGrid, Layout, Hexagon, GridGenerator, Pattern } from 'react-hexgrid';
import './App.css';


class Board extends Component {
    render() {
        const hexagons = GridGenerator.hexagon(2);
        const hexagonSize = { x: 10, y: 10 };
        return (
          <div className="App">
            <HexGrid  width={1200} height={1000}>
            <Pattern id="pic" link ="/images/clayHex.png" size={hexagonSize}/>
            <defs></defs>
              <Layout size={hexagonSize}spacing={1.009} flat={false} origin={{ x: 0, y: 0 }}>
                { hexagons.map((hex, i) => <Hexagon key={i} q={hex.q} r={hex.r} s={hex.s} fill="pic" />) }
              </Layout>
            </HexGrid>
          </div>
        );
      }
}

export default Board;