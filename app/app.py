from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/')
def inicio():
    return "<h1>Hello world</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)