import myApp.modelSQL as sql
from hashlib import sha256

def properLogin(form):
    conn, cursor = sql.open()
    if conn==None or cursor==None:
        return "Login page error"
    else:
        username = form.username.data
        email = form.email.data
        password = sha256(form.password.data.encode()).hexdigest()
        password = form.password.data

        query = """
            SELECT COUNT(*) AS count FROM Users WHERE username={} AND password_hash={};
            """.format((username, password))

        cursor.execute(query)
        print(list(cursor))


def properSignup(form):
    conn, cursor = sql.open()
    if conn==None or cursor==None:
        return False
    else:
        username = form.username.data
        email = form.email.data
        password = sha256(form.password.data.encode()).hexdigest()

        query = """
        SELECT * FROM Users WHERE username=? OR email=?
        """
        cursor.execute(query, (username, email))
        count = cursor.rowcount
        #print("value of count is ", count)
        if count == 0:
            return properInsertForm(form, conn, cursor)
        else:
            return False

def properInsertForm(form, conn, cursor):
    email = form.email.data
    password = sha256(form.password.data.encode()).hexdigest()
    username = form.username.data

    print("inside insert")
    sql.insert_data_Users(username, email, password)
    sql.close()
    return True
