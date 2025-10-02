# config.py
import mysql.connector

class Config:
    SECRET_KEY = "yoursecretkey123"   # change this later
    DB_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "sunbeam",
        "database": "schools"
    }

def get_db_connection():
    return mysql.connector.connect(**Config.DB_CONFIG)
