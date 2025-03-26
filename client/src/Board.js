import React, { Component } from 'react';
import {
  HexGrid, Layout, Hexagon, GridGenerator, Pattern
} from 'react-hexgrid';
class Board extends Component {
  render() {
    const hexagons = GridGenerator.hexagon(2);
    const hexSize = { x: 10, y: 10 };
    const fields = ["Desert", "Ore", "Ore", "Ore", "Clay", "Clay", "Clay", "Wheat", "Wheat", "Wheat", "Wheat", "Sheep", "Sheep", "Sheep", "Sheep", "Wood", "Wood", "Wood", "Wood",]
    return (
      <div className="App">
        <HexGrid width={1200} height={1000}>
          <defs>
            <Pattern id="Desert" link="/images/desertHex.png"/>
            <Pattern id="Ore" link="/images/oreHex.png"/>
            <Pattern id="Clay" link="/images/clayHex.png"/>
            <Pattern id="Wheat" link="/images/wheatHex.png"/>
            <Pattern id="Sheep" link="/images/sheepHex.png"/>
            <Pattern id="Wood" link="/images/woodHex.png"/>

          </defs>
          
          <Layout
            size={hexSize}
            spacing={1.009}
            flat={false}
            origin={{ x: 0, y: 0 }}
          >
            {hexagons.map((hex, i) => {
                const fieldType = fields[i]
                return (<Hexagon key={i} q={hex.q} r={hex.r} s={hex.s} fill={fieldType}/>);
            }

            )}
          </Layout>
        </HexGrid>
      </div>
    );
  }
}

export default Board;
