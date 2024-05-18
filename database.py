import sqlite3

conn = sqlite3.connect("websiteDataBase.sqlite")

cursor = conn.cursor()

# Create the product table
#sql_query = "CREATE TABLE product(id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INTEGER NOT NULL, image TEXT NOT NULL, quantity INTEGER NOT NULL)"
#cursor.execute(sql_query)

# Function to add data to the database

def add_to_database(id, name, price, image, quantity, tablename):
    sqliteConnection = sqlite3.connect("websiteDataBase.sqlite")
    cursor = sqliteConnection.cursor()
    empPhoto = ''
    # Assuming image is a file path, you can directly store it as text
    data_tuple = (id, name, price, empPhoto, quantity)
    
    sql_query = "INSERT INTO " + str(tablename) + " VALUES (?, ?, ?, ?, ?)"
    
    cursor.execute(sql_query, data_tuple)
    sqliteConnection.commit()
    cursor.close()

def delete_from_database(id, tablename):
    sqliteConnection = sqlite3.connect("websiteDataBase.sqlite")
    cursor = sqliteConnection.cursor()

    sql_query = "DELETE FROM " + str(tablename) + " WHERE id =" + str(id) 
    cursor.execute(sql_query)
    sqliteConnection.commit()
    cursor.close()

def return_all_the_table(tablename):
    conn = sqlite3.connect("websiteDataBase.sqlite")
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM " + str(tablename))
    products = [
        dict(id=row[0], name=row[1], price=row[2], image= '',quantity=row[4])
        for row in cursor.fetchall()
    ]
    if products is not None:
        return products

def return_by_id(id, tablename):
    conn = sqlite3.connect("websiteDataBase.sqlite")
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM " + str(tablename) + " WHERE id = " + str(id))
    row = cursor.fetchone()
    if row:
        product_dict = {
            'id': row[0],
            'name': row[1],
            'price': row[2],
            'image': '',
            'quantity': row[4]
        }
        return product_dict
    else:
        return None

def creat_table(tablename):
    conn = sqlite3.connect("websiteDataBase.sqlite")
    cursor = conn.cursor()

    cursor = conn.execute("CREATE TABLE " + str(tablename) + "(id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INTEGER NOT NULL, image TEXT NOT NULL, quantity INTEGER NOT NULL)")
    cursor.close()

# Add a sample record to the database
#add_to_database(1, "Product 2", 500, "photos/product1.jpg", 1)

#creat_table('cart_product')
#delete_from_database(2, 'cart_product')