from flask import Flask, json, jsonify
from flask_cors import CORS
from room_service import RoomService
from book_service import BookService
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
  return "Successfully Signed Out."

def reserve_room(room_id: str):
  room_service = RoomService()
  # room_service.reserve_room(room_id)
  pass

def rooms():
  room_service = RoomService()
  print(room_service.find_all())

def books():
  book_service = BookService()
  print(book_service.find_all())

def checkout_book(book_id: str):
  # TODO: missing implementation
  pass

if __name__ == "__main__":
    app.run()