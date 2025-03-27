from flask import Flask, jsonify
import random
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/fields")
def members():
    fields = ["Desert", "Ore", "Ore", "Ore", "Clay", "Clay", "Clay", "Wheat", "Wheat", "Wheat", "Wheat", "Sheep", "Sheep", "Sheep", "Sheep", "Wood", "Wood", "Wood", "Wood",]
    random.shuffle(fields)
    print(fields)
    return jsonify(fields)

if __name__ == "__main__":
    app.run(debug=True)