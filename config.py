"""This module is to configure app to connect with database."""

from pymongo import MongoClient

DATABASE = MongoClient()['smarthome'] # DB_NAME
DEBUG = True
client = MongoClient('mongodb://ilham:ilham123@localhost/smarthome?authSource=admin')

