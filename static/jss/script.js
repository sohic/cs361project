function updateTime() {
    var dateTimeElement = document.getElementById('datetime');
    var timezoneElement = document.getElementById('locationTZ');
    var currentDateTime = new Date().toLocaleString("en-US", { timeZone: timezoneElement.textContent });
  
    var dateObj = new Date(currentDateTime);
    var dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var dayIndex = dateObj.getDay();
    var monthIndex = dateObj.getMonth();
    var day = dateObj.getDate();
    var year = dateObj.getFullYear();
    var hours = dateObj.getHours();
    var minutes = dateObj.getMinutes();
    var seconds = dateObj.getSeconds();
    var timeZoneOffset = dateObj.getTimezoneOffset();
    var timeZoneOffsetHours = Math.floor(Math.abs(timeZoneOffset) / 60);
    var timeZoneOffsetMinutes = Math.abs(timeZoneOffset) % 60;
    var timeZoneOffsetSign = timeZoneOffset < 0 ? "+" : "-";
    var timeZoneOffsetString = `GMT${timeZoneOffsetSign}${timeZoneOffsetHours.toString().padStart(2, '0')}${timeZoneOffsetMinutes.toString().padStart(2, '0')}`;
    var timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
  
    // Convert to 12-hour clock
    var ampm = hours < 12 ? "AM" : "PM";
    hours = hours % 12;
    if (hours === 0) {
      hours = 12;
    }
  
    // Add leading zeros if needed
    minutes = (minutes < 10) ? '0' + minutes : minutes;
    seconds = (seconds < 10) ? '0' + seconds : seconds;
  
    // Update the date and time in the span element
    dateTimeElement.textContent = `${dayNames[dayIndex]} ${monthNames[monthIndex]} ${day} ${year} ${hours}:${minutes}:${seconds} ${ampm}`;
  }
  
  // Call updateTime function every second
  setInterval(updateTime, 1000);

function showAlert(){
    alert(document.getElementById('locationHome').value)
}


function updateTemperatureUnitLabel() {
    var temperatureUnitLabel = document.getElementById('temperatureUnitLabel');
    var centigradeRadio = document.getElementById('centigrade');
    var fahrenheitRadio = document.getElementById('fahrenheit');
    var unit;
    if (centigradeRadio.checked){
        unit = "°C";
    }
    else {
        unit = "°F";
    }
    temperatureUnitLabel.textContent = unit;
}
updateTemperatureUnitLabel();



// Function to fill the table with temperature data
function fillWeatherTable() {
document.getElementById('currentTemp').textContent = weatherData.current + '°'; // Append temperature unit
document.getElementById('day2Temp').textContent = weatherData.day2 + '°';
document.getElementById('day3Temp').textContent = weatherData.day3 + '°';
document.getElementById('day4Temp').textContent = weatherData.day4 + '°';
document.getElementById('day5Temp').textContent = weatherData.day5 + '°';
document.getElementById('day6Temp').textContent = weatherData.day6 + '°';
document.getElementById('day7Temp').textContent = weatherData.day7 + '°';
}

// Call the function to fill the table
fillWeatherTable();

const homeIconHourly = document.querySelector('img[alt="Home"]');

// Add event listener for click event
homeIconHourly.addEventListener('click', function() {
    // Redirect to /home
    window.location.href = '/';
});


const searchIconTen = document.querySelector('img[alt="Search"]');

// Add event listener for click event
searchIconTen.addEventListener('click', function() {
    // Redirect to /home
    window.location.href = '/search';
});

function displaySelectedOption() {
    var selectedOption = document.querySelector('input[name="displayOption"]:checked').value;
    if (selectedOption === "hourly") {
        window.location.href = "/hourly";
    } else if (selectedOption === "weekly") {
        window.location.href = "/weekly";
    } 
}

function cancelForm() {
    document.getElementById("myForm").reset();
    window.location.href = "/";
}