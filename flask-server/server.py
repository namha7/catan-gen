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
    coordinates = [
        {"q": 0, "r": -2, "s": 2},
        {"q": 1, "r": -2, "s": 1},
        {"q": 2, "r": -2, "s": 0},
        {"q": -1, "r": -1, "s": 2},
        {"q": 0, "r": -1, "s": 1},
        {"q": 1, "r": -1, "s": 0},
        {"q": 2, "r": -1, "s": -1},
        {"q": -2, "r": 0, "s": 2},
        {"q": -1, "r": 0, "s": 1},
        {"q": 0, "r": 0, "s": 0},
        {"q": 1, "r": 0, "s": -1},
        {"q": 2, "r": 0, "s": -2},
        {"q": -2, "r": 1, "s": 1},
        {"q": -1, "r": 1, "s": 0},
        {"q": 0, "r": 1, "s": -1},
        {"q": 1, "r": 1, "s": -2},
        {"q": -2, "r": 2, "s": 0},
        {"q": -1, "r": 2, "s": -1},
        {"q": 0, "r": 2, "s": -2}
        ]

    random.shuffle(fields)
    random.shuffle(numbers)
    random.shuffle(coordinates)

    boardData = []
    num_index = 0
    for i in range(len(fields)):
        field_type = fields[i]
        coordinate = coordinates[i]
        if field_type == "Desert":
            number = None
        else: 
            number = numbers[num_index]
            num_index += 1

        boardData.append({
            "type": field_type,
            "number": number,
            "coordinates": coordinate
        })
    return jsonify(boardData)


if __name__ == "__main__":
    app.run(debug=True)