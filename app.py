#app.py

from flask import Flask, request, jsonify
from service import ToDoService
from models import Schema
import json

app = Flask(__name__)

@app.route("/")
def hello():
	return "TO DO LIST"

@app.route("/<name>")
def hello_name(name):
	return "Hello" + name

@app.route("/todo", methods=["POST"])
def create_todo():
	return jsonify(ToDoService().create(request.get_json()))

@app.route("/todo", methods=["GET"])
def get_todo():
	return jsonify(ToDoService().select_by_id())

@app.route("/todo/<item_id>", methods=["PUT"])
def update_todo(item_id):
	return jsonify(ToDoService.update(item_id, request.get_json()))

@app.route("/todo/<item_id>", methods=["DELETE"]):
	return jsonify(ToDoService.delete(item_id))


if __name__ == "__main__":
	Schema()
	app.run()