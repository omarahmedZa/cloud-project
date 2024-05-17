from flask import Flask, request, jsonify, render_template, url_for, redirect, session
import sqlite3
import json
import base64
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
    conn = db_connection()
    cursor = conn.cursor()

    cursor = conn.execute("SELECT * FROM product")
    products = [
        dict(id=row[0], name=row[1], price=row[2], image=base64.b64encode(row[3]).decode('utf-8') if isinstance(row[3], bytes) else None,quantity=row[4])
        for row in cursor.fetchall()
    ]
    if products is not None:
        return render_template('index.html', products=products)

@app.route("/cart_management", methods=['GET'])
def cart_management():    

    return render_template('frontend.html', data=all_data)
    '''products = []
    conn = db_connection()
    cursor = conn.cursor()
    for i in all_data:
        print[i]
        cursor.execute("SELECT * FROM product WHERE id = ?", (i,))
        row = cursor.fetchone()
        if row:
            products.append(dict(id=row[0], name=row[1], price=row[2], image=base64.b64encode(row[3]).decode('utf-8') if isinstance(row[3], bytes) else None, quantity=row[4]))
    
    conn.close()
    
    return render_template('frontend.html', products=products)'''
    '''if data:
        products = []
        conn = db_connection()
        cursor = conn.cursor()
        for i in data:
            cursor.execute("SELECT * FROM product WHERE id = ?", (i,))
            row = cursor.fetchone()
            if row:
                products.append(dict(id=row[0], name=row[1], price=row[2], image=base64.b64encode(row[3]).decode('utf-8') if isinstance(row[3], bytes) else None, quantity=row[4]))
        
        conn.close()
        if products:
            return render_template('frontend.html', products=products)
        else:
            return jsonify({"error": "No products found"}), 404
    else:
        return jsonify({"error": "No data provided"}), 400'''
    
@app.route("/cart_management", methods=['POST'])
def cart_management_POST():
    if request.method == 'POST':
        data = list(request.form.values())
        #jso = json.loads(jsonify(data))
        
        all_data.append(data)
        return(all_data)

@app.route("/data", methods=['POST'])
def data():
    if request.method == 'POST':
        data = list(request.form.values())
        #jso = json.loads(jsonify(data))
        
        all_data.append(data)    
        #return redirect(url_for("cart_management", data=data))
        '''if all_data:
            products = []
            conn = db_connection()
            cursor = conn.cursor()
            for i in all_data:
                cursor.execute("SELECT * FROM product WHERE id = ?", (i[0],))
                row = cursor.fetchone()
                if row:
                    products.append(dict(id=row[0], name=row[1], price=row[2], image=base64.b64encode(row[3]).decode('utf-8') if isinstance(row[3], bytes) else None, quantity=row[4]))
            
            conn.close()
            if products:
                return render_template('frontend.html', products=products)
            else:
                return jsonify({"error": "No products found"}), 404
        else:
            return jsonify({"error": "No data provided"}), 400'''
    


if __name__ == "__main__":
    app.run(debug=True)




