from flask import Flask,request,jsonify,render_template
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# #routing application to link the backend to the host(front End)

# new route the same basic route but give him name after /
# @app.route('/<name>')
# def print_name(name):
#     return 'Welcome,{}'.format(name)
# create list by jason
# Users = [
#     {
#         "id":0,
#         "username":"Ahmed",
#         "password":"123",
#     },
#     {
#         "id":1,
#         "username":"mohammed",
#         "password":"456",
#     }
# ]
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("User.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/log')
def index():
    return render_template('log.html')

@app.route('/signin')
def signin():
    return render_template('index.html')

@app.route('/users', methods=["GET", "POST"])
def Users_GetData():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM Users")
        users =[
            dict(id=row[0], username=row[1], password=row[2], email=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)

    if request.method == "POST": # Create new user
        new_username =request.json['username']
        new_pass = request.json['password']
        email = request.json['email']


        sql = """INSERT INTO Users (username, password, email)
                 VALUES(?,?,?)"""
        cursor = cursor.execute(sql, (new_username, new_pass, email))
        conn.commit()
        return f"Users with id:{cursor.lastrowid} created successfully", 201


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def signle_user(id):
    conn = db_connection()
    cursor = conn.cursor()
    user = None
    if request.method == "GET":  # to get singel user by id
        cursor.execute("SELECT * FROM Users WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            user = r
        if user is not None:
            return jsonify(user), 200
        else:
            return "something wrong", 404

    if request.method == "PUT":  # to update single user
        sql = """UPDATE Users 
                 SET username=?,
                     password=?,
                     email=?
                 WHERE id=?"""

        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]

        update_user = {
            "id": id,
            "username": username,
            "password": password,
            "email": email,
        }
        conn.execute(sql, (username, password, email, id))
        conn.commit()
        return jsonify(update_user)

    if request.method == "DELETE":
        sql = """DELETE FROM users WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been deleted.".format(id), 200



@app.route('/login', methods=["POST"])
def Users_login():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST": # Create new user

        data = request.json
        new_username = data.get('username')
        new_pass = data.get('password')

        cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (new_username, new_pass))
        user = cursor.fetchone()

        if user:
            # User found, login successful
            return jsonify({'message': 'Login successful'}), 201
        else:
            # User not found, login failed
            return jsonify({'error': 'Invalid username or password'}), 401




#programmtically way to run the app


if __name__ == '__main__':
    app.run(debug=True)
