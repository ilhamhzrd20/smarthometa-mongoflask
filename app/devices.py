"""This module will serve the api request."""

from config import client
from app import app
from bson.json_util import dumps, ObjectId
from flask import request, jsonify, Response
import json
import ast
from importlib.machinery import SourceFileLoader


# Import the helpers module
helper_module = SourceFileLoader('*', './app/helpers.py').load_module()

# Select the database
db = client.iot
# Select the collection
collection = db.devices

@app.route("/api/v1/devices", methods=['GET'])
def view_devices():
  try:
    if collection.find().count() > 0:
        # Prepare response if the users are found
        return Response(dumps(collection.find()), status=200, mimetype='application/json')
    else:
        # Return empty array if no users are found
        return Response(jsonify([]), status=200, mimetype='application/json')
  except:
    return "", 500

@app.route("/api/v1/devices/<device_id>", methods=['GET'])
def view_device(device_id):
  try:
    record_find = collection.find_one({"_id": ObjectId(device_id)})

    return Response(dumps(record_find), status=200, mimetype='application/json')
  except:
    return "", 500

@app.route("/api/v1/devices", methods=['POST'])
def create_devices():
  try:
    data = request.get_json()

    record_created = collection.insert(data)

    return Response(str(record_created), status=201, mimetype='application/json')
  except:
    return "", 500

@app.route("/api/v1/devices/<device_id>", methods=['PUT'])
def update_devices(device_id):
  try:
    data = request.get_json()
    records_updated = collection.update_one(
      {"_id": ObjectId(device_id)}, 
      {"$set": data})

    if records_updated.modified_count > 0:
        return "", 200
    else:
        return "", 404
  except:
    return "", 500

    