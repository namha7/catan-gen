# catan-gen
![image](https://github.com/user-attachments/assets/00a8cb1c-4658-4463-abe8-f0e908eaacbe)

A tool for generating fair Catan boards. It generates a board following these principles:

1. No two Ore/Brick tiles can touch    
2. No three Sheep/Wheat/Wood tiles can touch
3. Numbers 6 and 8 cannot touch
4. No two of the same number can touch


## Setup

### React (Frontend)
#### Prerequisities 
- Node.js
- npm
#### Steps
```bash
cd client
```
```bash
npm install
```
```bash
npm start
```

### Python Flask
#### Prerequisities 
- Python 3.8+
- pip
#### Steps
```bash
cd flask-server
```
```bash
python -m venv venv
```
activate virtual environment:
windows:
```bash
venv\Scripts\activate
```
mac:
```
source venv/bin/activate
```
install dependencies:
```
pip install Flask
pip install flask-cors
```
starting the server:
```
python server.py
```


Access the site via http://localhost:3000/
