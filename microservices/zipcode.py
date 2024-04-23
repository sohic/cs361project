from flask import Flask, jsonify
from uszipcode import SearchEngine

app = Flask(__name__)

@app.route("/zip", methods=['GET'])
def get_zip():
    engine = SearchEngine()
    zipcode = engine.by_zipcode(98275)
    location_info = {"zipcode":zipcode.zipcode, "city":zipcode.major_city, "state":zipcode.state_abbr}
    return jsonify(location_info)

if __name__ == "__main__":
    app.run(port=8003)