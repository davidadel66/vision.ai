from flask import Flask, jsonify, request
from stock_universe import stockUniverse

app = Flask(__name__)

@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    stock = stockUniverse(symbol)
    data = {
        "daily_data": stock.get_daily_data().to_dict(),
        "returns": stock.get_returns().to_list(),
        "earnings_reports": stock.get_earnings_reports().to_dict(),
        "fundamentals": stock.get_fundamentals(),
        # Add more data as needed
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)