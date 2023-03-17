from flask import Flask, render_template
import json
import os

app = Flask(__name__)

f = open('products.json')
 
products = json.load(f)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home_layout.html', title="Home")
  
@app.route('/about')
def about():
    return render_template('about_layout.html', title="About")

@app.route('/products')
def get_products():
    return render_template('products_layout.html', products=products, title='Products')
  
if __name__ == '__main__':  
    app.run(debug=True) 