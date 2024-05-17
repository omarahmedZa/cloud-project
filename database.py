import sqlite3

conn = sqlite3.connect("websiteDataBase.sqlite")

cursor = conn.cursor()

# Create the product table
#sql_query = "CREATE TABLE product(id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INTEGER NOT NULL, image TEXT NOT NULL, quantity INTEGER NOT NULL)"
#cursor.execute(sql_query)

# Function to add data to the database

sql_query = "SELECT * FROM product"
cursor = conn.execute(sql_query)

print ("ID\t\t\tName\t\t\t\tprice\t\t\timage\t\t\tquantity")
print (95 * "-")
for row in cursor:
    print("%5s%30s%30s%30s%30s" % (str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])))
    
print ("\n\n")

def add_to_database(id, name, price, image, quantity):
    sqliteConnection = sqlite3.connect("websiteDataBase.sqlite")
    cursor = sqliteConnection.cursor()
    
    with open(image, 'rb') as file:
        empPhoto = file.read()

    # Assuming image is a file path, you can directly store it as text
    data_tuple = (id, name, price, empPhoto, quantity)
    
    sql_query = "INSERT INTO product VALUES (?, ?, ?, ?, ?)"
    
    cursor.execute(sql_query, data_tuple)
    sqliteConnection.commit()
    cursor.close()

def delete_from_database(id):
    sqliteConnection = sqlite3.connect("websiteDataBase.sqlite")
    cursor = sqliteConnection.cursor()

    sql_query = "DELETE FROM product WHERE id =" + str(id) 
    cursor.execute(sql_query)
    sqliteConnection.commit()
    cursor.close()

def return_all_the_products():
    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM product")
    products = [
        dict(id=row[0], name=row[1], price=row[2], image=base64.b64encode(row[3]).decode('utf-8') if isinstance(row[3], bytes) else None,quantity=row[4])
        for row in cursor.fetchall()
    ]

# Add a sample record to the database
add_to_database(1, "Product 2", 500, "photos/product1.jpg", 1)


