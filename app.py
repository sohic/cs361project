from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/<zipcode>')
def home(zipcode):
    # URL of the first microservice to fetch zip code
    zip = f"https://cs361getzip-07f82c667655.herokuapp.com/{zipcode}"
    # Fetch the zip code data from the first microservice
    zipResponse = requests.get(zip)
    if zipResponse.status_code == 200:
        zipData = zipResponse.json()
        zipcode = zipData.get('zipcode')  # Extracting the zip code from the response
    else:
        return jsonify({'error': 'Failed to fetch zip code data'}), 500

    # URL of the weather microservice
    weatherInfo = f"https://cs361weather-39533f33981a.herokuapp.com/{zipcode}"
    # Fetch the weather data from the weather microservice
    weatherResponse = requests.get(weatherInfo)
    if weatherResponse.status_code == 200:
        weatherData = weatherResponse.json()  # Assuming the weather microservice returns JSON data
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

    # # Render the Jinja2 template, passing the weather data
    return render_template('main.j2', location=zipData, weather=weatherData)

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
