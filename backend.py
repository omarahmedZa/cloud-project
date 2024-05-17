from flask import Flask, request, jsonify, render_template, url_for, redirect, session
import sqlite3
import json
import base64
import database
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

all_data = []

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("websiteDataBase.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn 

@app.route("/product_catalog", methods=['GET'])
def product_catalog():
    products = []
    products = database.return_all_the_table
    if products is not None:
        return render_template('Product.html', products=products)

@app.route("/cart_management", methods=['GET'])
def cart_management():  
    products = database.return_all_the_table('cart_product')
    if products:
        return render_template('frontend.html', products=products)
    else:
        return jsonify({"error": "No products found"}), 404

@app.route("/save_cart_product", methods=['POST'])
def data():
    if request.method == 'POST':
        data = list(request.form.values())
        print(data[0])
        product = database.return_by_id(int(data[0]), 'product')
        database.add_to_database(product['id'], product['name'], product['price'], product['image'], product['quantity'], 'cart_product')
    return database.return_all_the_table('cart_product')
    


if __name__ == "__main__":
    app.run(debug=True)




