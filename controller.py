from flask import Flask, json, jsonify
from flask_cors import CORS
import typing

app = Flask(__name__)
CORS(app)

@app.route("/")
def test():
  return "Welcome to Hekman!"

def login(name: str) :
  # TODO: missing implementation
  pass

def logout(name: str) :
  # TODO: missing implementation
  pass

def reserve_room(room_id: str):
  # TODO: missing implementation
  pass

def rooms():
  # TODO: missing implementation
  pass

def books():
  # TODO: missing implementation
  pass

def checkout_book(book_id: str):
  # TODO: missing implementation
  pass

if __name__ == "__main__":
    app.run()