from flask import Flask, jsonify, request

app = Flask(__name__)

# exchange rate
def USDtoEuroRate():
    return 0.94  

@app.route('/usdtoeuros', methods=['GET'])
def convert_usd_to_euro():
    usd = request.args.get('amount', default=1, type=float)
    exchangeRate = USDtoEuroRate()
    euros = usd * exchangeRate
    return jsonify({
        'usd': usd,
        'euros': round(euros, 2),
        'exchangeRate': exchangeRate
    })

if __name__ == '__main__':
    app.run(debug=True, port=8006)