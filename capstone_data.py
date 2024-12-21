from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("recommendations_database.csv")

# API endpoint to fetch the description and price for a given StockCode
@app.route('/product/<string:stock_code>', methods=['GET'])
def get_product_details(stock_code):
    try:
        # Filter rows where StockCode matches the input (as a string)
        matching_rows = df[df['StockCode'].astype(str) == stock_code]

        if matching_rows.empty:
            # Return error if no matching StockCode is found
            return jsonify({"error": f"No details found for StockCode: {stock_code}"}), 404

        # Get the first matching description and price
        description = matching_rows['Description'].iloc[0]
        price = matching_rows['Price'].iloc[0]

        return jsonify({
            "Description": description,
            "Price": price
        })

    except KeyError:
        # Return error if the required columns are missing
        return jsonify({"error": "Dataset does not contain the required columns 'StockCode', 'Description', or 'Price'"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
