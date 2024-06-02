from flask import Flask, render_template, jsonify, request, make_response
import requests, json
from datetime import datetime
import pytz
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# global variables w/ default values
gZip = "98275"
gCity = "Mukilteo"
gState = "WA"
gTimeZone = "America/Los_Angeles"

def get_current_time():
    tz = pytz.timezone(gTimeZone)
    time = datetime.now(tz)
    #time = systemTime.astimezone(pytz.timezone(gTimeZone))
    current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')
    return current_datetime

@app.route('/')
def home():
    global gZip, gCity, gState, gTimeZone
    location = {'zipcode': gZip, 'city': gCity, 'state': gState, 'timezone': gTimeZone}
    
    # URL of the weather microservice
    weatherInfo = f"https://cs361weather-39533f33981a.herokuapp.com/{gZip}"
    # Fetch the weather data from the weather microservice
    weatherResponse = requests.get(weatherInfo)
    logger.info('Outgoing request: %s', weatherResponse.request.url)
    if weatherResponse.status_code == 200:
        weatherData = weatherResponse.json()  # Assuming the weather microservice returns JSON data
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    current_datetime = get_current_time()
    
    return render_template('home.j2', location=location, current_datetime=current_datetime, weather=weatherData)

#################################################################################################################################
@app.route('/display')
def display():
    global gZip, gCity, gState, gTimeZone
    location = {'zipcode': gZip, 'city': gCity, 'state': gState, 'timezone': gTimeZone}
    
    # URL of the weather microservice
    weatherInfo = f"https://cs361weather-39533f33981a.herokuapp.com/{gZip}"
    # Fetch the weather data from the weather microservice
    weatherResponse = requests.get(weatherInfo)
    if weatherResponse.status_code == 200:
        weatherData = weatherResponse.json()  # Assuming the weather microservice returns JSON data
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    current_datetime = get_current_time()
    
    return render_template('display.j2', location=location, current_datetime=current_datetime, weather=weatherData)

###################################################################################################################################
@app.route('/hourly')
def hourly():
    global gZip, gCity, gState, gTimeZone
    location = {'zipcode': gZip, 'city': gCity, 'state': gState, 'timezone': gTimeZone}
    current_datetime = get_current_time()
    
    hourly = f"https://cs361hourly-cc75e39efe2a.herokuapp.com/coord/{gZip}"
    logger.info('Outgoing request: %s', hourly.request.url)
    hourlyResponse = requests.get(hourly)
    if hourlyResponse.status_code == 200:
        hourlyData = hourlyResponse.json()
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    return render_template('hourly.j2', location=location, current_datetime=current_datetime, hourly=hourlyData)

#######################################################################################################################################
@app.route('/help')
def help():

    return render_template('help.j2')

#######################################################################################################################################
@app.route('/weekly')
def weekly():
    global gZip, gCity, gState, gTimeZone
    location = {'zipcode': gZip, 'city': gCity, 'state': gState, 'timezone': gTimeZone}
    current_datetime = get_current_time()
    
    weekly = f"https://cs361daily-20f4b9580bce.herokuapp.com//coord/{gZip}"
    weeklyResponse = requests.get(weekly)
    logger.info('Outgoing request: %s', weeklyResponse.request.url)
    if weeklyResponse.status_code == 200:
        weeklyData = weeklyResponse.json()
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    return render_template('weekly.j2', location=location, current_datetime=current_datetime, weekly=weeklyData)

########################################################################################################################################
@app.route('/search')
def search():
    global gZip, gCity, gState, gTimeZone
    location = {'zipcode': gZip, 'city': gCity, 'state': gState, 'timezone': gTimeZone}
    current_datetime = get_current_time()
    return render_template('search.j2', location=location, current_datetime=current_datetime)

##########################################################################################################################################
@app.route('/submit_location', methods=['POST'])
def submit_location():
    global gZip, gCity, gState, gTimeZone
    zipcode = request.form['zipcode']
    if (zipcode != ""):
        zip = f"https://cs361getzip-07f82c667655.herokuapp.com/{zipcode}"
        zipResponse = requests.get(zip)
        if zipResponse.status_code == 200:
            zipData = zipResponse.json()
            gZip = zipData.get('zipcode')  # Extracting the zip code from the response
            gCity = zipData.get('city')
            gState = zipData.get('state')
        else:
            message = "Invalid zipcode! Enter a valid US zipcode"
            response = make_response(f"""
            <script>
                alert('{message}');
                setTimeout(function(){{window.location.href = '/search'}}, 100);
            </script>
            """)
            return response

    # URL of the weather microservice
    weatherInfo = f"https://cs361weather-39533f33981a.herokuapp.com/{gZip}"
    # Fetch the weather data from the weather microservice
    weatherResponse = requests.get(weatherInfo)
    if weatherResponse.status_code == 200:
        weatherData = weatherResponse.json()  # Assuming the weather microservice returns JSON data
        gTimeZone = weatherData["timezone"]
    else:
        message = "Weather microservice is currently offline."
        response = make_response(f"""
        <script>
            alert('{message}');
            setTimeout(function(){{window.location.href = '/search'}}, 100);
        </script>
        """)
        return response
    
    zipDataFinal = {
        'zipcode': gZip,
        'city': gCity,
        'state': gState,
        'timezone': gTimeZone
    }

    current_datetime = get_current_time()
    return render_template('home.j2', location=zipDataFinal, weather=weatherData, current_datetime=current_datetime)

################################################################################################################################
@app.route('/convert', methods=['POST'])
def convert_temperature():
    data = request.get_json()
    temperature = data['temperature']
    is_fahrenheit = data['isFahrenheit']

    if is_fahrenheit:
        convert = f"https://chenbry.pythonanywhere.com/c2f?values={temperature}"
        convertResponse = requests.get(convert)
        logger.info('Outgoing request: %s', convertResponse.request.url)
        if convertResponse.status_code == 200:
            newData = convertResponse.json()
            new_temp = newData['fahrenheit_values'][0]
    else:
        # Convert Fahrenheit to Celsius
        new_temp = (temperature - 32) * 5/9

    # The new temperature is rounded to two decimal places
    return jsonify(temperature=round(new_temp, 2))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
