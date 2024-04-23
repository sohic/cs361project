from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # URL of the first microservice to fetch zip code
    # zip_url = "http://localhost:8003/zip"
    # # Fetch the zip code data from the first microservice
    # zip_response = requests.get(zip_url)
    # if zip_response.status_code == 200:
    #     zip_data = zip_response.json()
    #     zipcode = zip_data.get('zipcode')  # Extracting the zip code from the response
    # else:
    #     return jsonify({'error': 'Failed to fetch zip code data'}), 500

    # # URL of the weather microservice
    # weather_url = f"http://localhost:8000/weather?zipcode={zipcode}"
    # # Fetch the weather data from the weather microservice
    # weather_response = requests.get(weather_url)
    # if weather_response.status_code == 200:
    #     weather_data = weather_response.json()  # Assuming the weather microservice returns JSON data
    # else:
    #     return jsonify({'error': 'Failed to fetch weather data'}), 500

    # # Render the Jinja2 template, passing the weather data
    # return render_template('main.j2', location=zip_data, weather=weather_data)
    return 'this is a test'

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
