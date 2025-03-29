import React, { Fragment, Component } from 'react';
import {
  HexGrid, Layout, Hexagon, GridGenerator, Pattern, Text
} from 'react-hexgrid';
import App from "./App"

class Board extends Component {
  render() {

    const hexagons = GridGenerator.hexagon(2);
    const hexSize = { x: 10, y: 10 };

    //const fields = ['Clay', 'Wood', 'Sheep', 'Sheep', 'Wood', 'Clay', 'Sheep', 'Wheat', 'Wheat', 'Wood', 'Ore', 'Wheat', 'Ore', 'Clay', 'Desert', 'Wheat', 'Ore', 'Sheep', 'Wood']
    var fields = this.props.fields
    
    
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
            {fields.map((field, i) => {
                var fieldType = field.type   
                var coordinate_q = field.coordinates.q
                var coordinate_r = field.coordinates.r
                var coordinate_s = field.coordinates.s
                return(<Hexagon key={i} q={coordinate_q} r={coordinate_r} s={coordinate_s} fill={fieldType}>
                    <Text>{field.number}</Text>
                </Hexagon> );
            }
            )} 
          </Layout>
        </HexGrid>
      </div>
    );
  }
}

export default Board;
