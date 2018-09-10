import sqlite3
from datetime import datetime

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def create_table_Users():
    query = """
    CREATE TABLE IF NOT EXISTS Users(
        username TEXT,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        PRIMARY KEY(username))
    """
    cursor.execute(query)

def create_table_History():
    query = """
    CREATE TABLE IF NOT EXISTS History(
        id INTEGER,
        username TEXT NOT NULL,
        search_query TEXT NOT NULL,
        at_time TEXT NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY(username) REFERENCES Users(username))
    """
    cursor.execute(query)

def insert_data_Users():
    query = """
        INSERT INTO Users(username, email, password_hash)
        VALUES('aayush', 'gmai', 'kachra')
        """
    conn.execute(query)
    conn.commit()

def insert_data_History():
    query = """
        INSERT INTO History(username, search_query, at_time) VALUES ('aayush', 'gool','rfff')
    """
    conn.execute(query)
    conn.commit()

insert_data_History()
