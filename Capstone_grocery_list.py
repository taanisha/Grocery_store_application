from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the recommendations database
data_path = "recommendations_database.csv"
recommendations_df = pd.read_csv(data_path)

# API to fetch all products in alphabetical order
@app.route('/api/products', methods=['GET'])
def get_products():
    products = sorted(recommendations_df['Description'].dropna().unique())
    return jsonify(products)

# In-memory grocery list
grocery_list = []

# API to add a product to the grocery list
@app.route('/api/add_to_grocery', methods=['POST'])
def add_to_grocery():
    product = request.json.get('product')
    if product not in grocery_list:
        grocery_list.append(product)
    return jsonify({"grocery_list": grocery_list})

# API to fetch the current grocery list
@app.route('/api/grocery_list', methods=['GET'])
def get_grocery_list():
    return jsonify(grocery_list)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
