from flask import Flask, jsonify
import random
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

boardDataDummy = [
    {
        "type": "Desert",
        "number": None,
        "coordinates": {"q": 0, "r": -2, "s": 2}
    },
        
    {
        "type": "Ore",
        "number": 2,
        "coordinates": {"q": 1, "r": -2, "s": 1}
    },
        
    {
        "type": "Ore",
        "number": None,
        "coordinates": {"q": 2, "r": -2, "s": 0}
    },
        
    {
        "type": "Ore",
        "number": None,
        "coordinates": {"q": -1, "r": -1, "s": 2}
    },
        
    {
        "type": "Clay",
        "number": None,
        "coordinates": {"q": 0, "r": -1, "s": 1}
    },
        
    {
        "type": "Clay",
        "number": None,
        "coordinates": {"q": 1, "r": -1, "s": 0}
    },
        
    {
        "type": "Clay",
        "number": None,
        "coordinates": {"q": 2, "r": -1, "s": -1}
    },
        
    {
        "type": "Wheat",
        "number": None,
        "coordinates": {"q": -2, "r": 0, "s": 2}
    },
        
    {
        "type": "Wheat",
        "number": None,
        "coordinates": {"q": -1, "r": 0, "s": 1}
    },
        
    {
        "type": "Wheat",
        "number": None,
        "coordinates": {"q": 0, "r": 0, "s": 0}
    },
        
    {
        "type": "Wheat",
        "number": None,
        "coordinates": {"q": 1, "r": 0, "s": -1}
    },
        
    {
        "type": "Wood",
        "number": None,
        "coordinates": {"q": 2, "r": 0, "s": -2}
    },
        
    {
        "type": "Wood",
        "number": None,
        "coordinates": {"q": -2, "r": 1, "s": 1}
    },
        
    {
        "type": "Wood",
        "number": None,
        "coordinates": {"q": -1, "r": 1, "s": 0}
    },
        
    {
        "type": "Wood",
        "number": None,
        "coordinates": {"q": 0, "r": 1, "s": -1}
    },
        
    {
        "type": "Sheep",
        "number": None,
        "coordinates": {"q": 1, "r": 1, "s": -2}
    },
        
    {
        "type": "Sheep",
        "number": None,
        "coordinates": {"q": -2, "r": 2, "s": 0}
    },
        
    {
        "type": "Sheep",
        "number": None,
        "coordinates": {"q": -1, "r": 2, "s": -1}
    },
        
    {
        "type": "Sheep",
        "number": None,
        "coordinates": {"q": 0, "r": 2, "s": -2}
    }
]

@app.route("/fields")
def members():
    fields = ["Desert", "Ore", "Ore", "Ore", "Clay", "Clay", "Clay", "Wheat", "Wheat", "Wheat", "Wheat", "Sheep", "Sheep", "Sheep", "Sheep", "Wood", "Wood", "Wood", "Wood",]
    numbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]

    random.shuffle(fields)
    print(fields)
    return jsonify(boardDataDummy)


if __name__ == "__main__":
    app.run(debug=True)