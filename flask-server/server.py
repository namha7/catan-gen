from flask import Flask, jsonify
import random
from flask_cors import CORS
import hex
import string


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

@app.route("/fields")
def members():
    attempts = 0
    fields = ["Desert", "Ore", "Ore", "Ore", "Clay", "Clay", "Clay", "Wheat", "Wheat", "Wheat", "Wheat", "Sheep", "Sheep", "Sheep", "Sheep", "Wood", "Wood", "Wood", "Wood",]
    numbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    print("##################################################################")
    boardData = generateBoardData(fields,numbers,coordinates)
    attempts += 1
    while doesSameNumberTouch(boardData) or doBrickTilesTouch(boardData) or doOreTilesTouch(boardData) or doesSheepHaveTwoNeighbors(boardData) or doesWoodHaveTwoNeighbors(boardData) or doesWheatHaveTwoNeighbors(boardData):
        boardData = generateBoardData(fields,numbers,coordinates)
        attempts += 1
    
    print("generated board after "+ str(attempts) + " attempts")
    return jsonify(boardData)

def generateBoardData(fields, numbers, coordinates):
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
    return boardData

hex_directions = [
    hex.Hex(1, 0, -1),
    hex.Hex(1, -1, 0),
    hex.Hex(0, -1, 1),
    hex.Hex(-1, 0, 1),
    hex.Hex(-1, 1, 0),
    hex.Hex(0, 1, -1)
]
# koordinaten in json format für bessere verarbeitung
def makeCoord(q,r,s):
    coord = {"q": q, "r": r, "s": s}
    return coord
# prüft ob koordinate im board ist
def isPartOfBoard(q,r,s):
    coord = makeCoord(q,r,s)
    print(coord)
    if coord not in coordinates:
        return False
    return True

def doesSameNumberTouch(boardData):
    numbersArray = [2,3,4,5,6,8,9,10,11,12]
    for number in numbersArray:
        numbers = []

        for i in range(len(boardData)):
            if boardData[i]["number"] == number:
                numbers.append(boardData[i])
        for tile in numbers:
            hexCoordinates = tile["coordinates"]
            q = hexCoordinates["q"]
            r = hexCoordinates["r"]
            s = hexCoordinates["s"]
            touchingNumbers = 0
            for direction in range(6):
                neighbor_q = hex.hex_neighbor(hex.Hex(q,r,s), direction).q
                neighbor_r = hex.hex_neighbor(hex.Hex(q,r,s), direction).r
                neighbor_s = hex.hex_neighbor(hex.Hex(q,r,s), direction).s
                if isPartOfBoard(neighbor_q,neighbor_r,neighbor_s):
                    for boardTile in boardData:
                        coord = boardTile["coordinates"]
                        if (coord["q"] == neighbor_q and
                            coord["r"] == neighbor_r and
                            coord["s"] == neighbor_s):
                            if boardTile["number"] == number:
                                touchingNumbers += 1
                            break
            if  touchingNumbers >= 1:
                return True
    return False
# bugged
def doSixAndEightTouch(boardData):

    for i in range(len(boardData)):
        
        if boardData[i]["number"] == 6 or boardData[i]["number"] == 8:
            numbers = []
            numbers.append(boardData[i])
    for tile in numbers:
        hexCoordinates = tile["coordinates"]
        q = hexCoordinates["q"]
        r = hexCoordinates["r"]
        s = hexCoordinates["s"]
        touchingSixAndEights = 0
        for direction in range(6):
            neighbor_q = hex.hex_neighbor(hex.Hex(q,r,s), direction).q
            neighbor_r = hex.hex_neighbor(hex.Hex(q,r,s), direction).r
            neighbor_s = hex.hex_neighbor(hex.Hex(q,r,s), direction).s
            if isPartOfBoard(neighbor_q,neighbor_r,neighbor_s):
                for boardTile in boardData:
                    coord = boardTile["coordinates"]
                    if (coord["q"] == neighbor_q and
                        coord["r"] == neighbor_r and
                        coord["s"] == neighbor_s):
                        if boardTile["number"] == 6 or boardTile["number"] == 8:
                            touchingSixAndEights += 1
                        break
        if touchingSixAndEights >= 1:
            return True
    return False
# boardData, tilesArray, neighborFieldType, numberOfNeighbors
# durch tilesarray iterieren und nachbarn in boardData finden, speichert den nachbarn in liste wenn er bestimmten typ neighborFieldType hat und gibt true wenn die liste so lang ist wie numberofneighbors
def hasNeighbor(boardData, tilesArray, neighborFieldType, numberOfNeighborsWithFieldType):
    
    # findet Koordinaten von den tiles im Array
    for tile in tilesArray:
        hexCoordinates = tile["coordinates"]
        q = hexCoordinates["q"]
        r = hexCoordinates["r"]
        s = hexCoordinates["s"]
        print("Looking for neighbors of tile:",q,r,s)
        neighborsWithFieldType = 0

        # guckt alle nachbarn für ein tile an
        for direction in range(6):
            neighbor_q = hex.hex_neighbor(hex.Hex(q,r,s), direction).q
            neighbor_r = hex.hex_neighbor(hex.Hex(q,r,s), direction).r
            neighbor_s = hex.hex_neighbor(hex.Hex(q,r,s), direction).s
            if isPartOfBoard(neighbor_q,neighbor_r,neighbor_s):
                for boardTile in boardData:
                    coord = boardTile["coordinates"]
                    if (coord["q"] == neighbor_q and
                        coord["r"] == neighbor_r and
                        coord["s"] == neighbor_s):
                        if boardTile["type"] == neighborFieldType:
                            neighborsWithFieldType += 1
                        break
                            

        if neighborsWithFieldType >= numberOfNeighborsWithFieldType:
            print("Tile at" + str(q) + str(r) + str(s) + "has" + str(numberOfNeighborsWithFieldType)+ "neighbors with type " + neighborFieldType)
            return True
        
    return False
        
def doesWoodHaveTwoNeighbors(boardData):
    woodTiles = []

    for i in range(len(boardData)):
        if boardData[i]["type"] == "Wood":
            woodTiles.append(boardData[i])
    return hasNeighbor(boardData, woodTiles, "Wood", 2)
    
def doesWheatHaveTwoNeighbors(boardData):
    wheatTiles = []

    for i in range(len(boardData)):
        if boardData[i]["type"] == "Wheat":
            wheatTiles.append(boardData[i])
    return hasNeighbor(boardData, wheatTiles, "Wheat", 2)

def doesSheepHaveTwoNeighbors(boardData):
    sheepTiles = []

    for i in range(len(boardData)):
        if boardData[i]["type"] == "Sheep":
            sheepTiles.append(boardData[i])
    return hasNeighbor(boardData, sheepTiles, "Sheep", 2)


## Alle Steinfelder in BoardData suchen und abspeichern
# alle Nachbarn in liste speichern
# wenn nachbarn feldtyp = stein enthalten;: false
# sonst true
def doOreTilesTouch(boardData): 
    oreTiles = []

    for i in range(len(boardData)):
        if boardData[i]["type"] == "Ore":
            oreTiles.append(boardData[i])
    return hasNeighbor(boardData, oreTiles, "Ore", 1)

def doBrickTilesTouch(boardData): 
    brickTiles = []

    for i in range(len(boardData)):
        if boardData[i]["type"] == "Clay":
            brickTiles.append(boardData[i])
    return hasNeighbor(boardData, brickTiles, "Clay", 1)
    



if __name__ == "__main__":
    app.run(debug=True)