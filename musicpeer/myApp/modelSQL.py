import sqlite3
from datetime import datetime

filename = "database.db"

# initiate database connection, cursors
def open(filename=filename):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        return conn, cursor
    except:
        return None, None

# close database connection
def close(conn):
    conn.close()

def create_table_Users(cursor):
    query = """
    CREATE TABLE IF NOT EXISTS Users(
        username TEXT,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        PRIMARY KEY(username))
    """
    cursor.execute(query)

def create_table_History(cursor):
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

def insert_data_Users(username, email, password_hash):
    query = """
        INSERT INTO Users(username, email, password_hash)
        VALUES(?, ?, ?)
        """
    conn.execute(query, (username, email, password_hash))
    conn.commit()

def insert_data_History(username, search_query):
    query = """
        INSERT INTO History(username, search_query, at_time) VALUES (?, ?, ?)
    """
    print()
    conn.execute(query, (datetime('now')))
    conn.commit()
