from flask import Flask, render_template
import json
import os

app = Flask(__name__)

f = open(r'/Users/michal/projects/python-applications/class_4/server/products.json')

products = json.load(f)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def get_products():
    return render_template('products_discount.html', products=products)
  
if __name__ == '__main__':  
    app.run(debug=True)