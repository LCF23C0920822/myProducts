import os
from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)

    # Conexión a MongoDB Atlas
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.shop_db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products_collection = db.products
    products = products_collection.find()
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)