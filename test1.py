import sqlite3

# a connection needes to be opened to the database
conn = sqlite3.connect("dummy.sqlite")
# cursor is an interface for querying the database
cursor = conn.cursor()

# create users table
def create_table_Users(cursor=cursor, conn=conn):
    query = """
    CREATE TABLE IF NOT EXISTS Users(
        name TEXT NOT NULL,
        username TEXT PRIMARY KEY NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password_hash CHAR(64) );
    """
    cursor.execute(query)
    # a connection must be closed when done reading/writing

# inseret into users table
def insert_into_Users(name, username, email, password_hash, cursor=cursor, conn=conn):
    create_table_Users()
    query = """
    INSERT INTO Users (name, username, email, password_hash) VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (name, username, email, password_hash))
    conn.commit()

# check if a email-password pair is present in Users table
def is_present_in_Users(email, password_hash, cursor=cursor, conn=conn):
    query = """
    SELECT * FROM Users WHERE email=? AND password_hash=?
    """
    cursor.execute(query, (email, password_hash))
    if cursor.rowcount == -1:
        return False
    count = 0
    for r in cursor:
        count += 1
    if count == 1:
        return True
    else:
        return False

def is_email_available(email, cursor=cursor, conn=conn):
    query="""
    SELECT * FROM Users WHERE email=?
    """
    cursor.execute(query, (email))
    if cursor.rowcount == -1:
        return False
    count = 0
    for r in cursor:
        count += 1
    if count > 0:
        return False
    else:
        return True

def is_username_available(username, cursor=cursor, conn=conn):
    query="""
    SELECT * FROM Users WHERE username=?
    """
    cursor.execute(query, (username))
    if cursor.rowcount == -1:
        return False
    count = 0
    for r in cursor:
        count += 1
    if count > 0:
        return False
    else:
        return True


#conn.close()
