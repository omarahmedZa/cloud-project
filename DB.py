import sqlite3

conn = sqlite3.connect("User.sqlite")
cursor = conn.cursor()
sql_query = """CREATE TABLE Users(
    id integer PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL,
    email text NOT NULL
)"""

cursor.execute(sql_query)