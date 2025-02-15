document.getElementById('weather-form').addEventListener('submit', handleClick);

// Handler function, decides which function to use based on selection of city
function handleClick(event) {
    event.preventDefault();
    var city = document.getElementById('city').value;
    if (city === "current") {
        getCurrentLocationWeather(); // Call function to get current location weather
    } else {
        getCityWeather(city); // Call function to get weather for existing city
    }
}

// Function to get weather for existing cities
function getCityWeather(city) {
    var office, gridX, gridY;
    // Define office and grid information for the cities using switch cases
    switch (city) {
        case "New York":
            office = "OKX";
            gridX = 33;
            gridY = 35;
            break;
        case "Boston":
            office = "BOX";
            gridX = 71;
            gridY = 90;
            break;
        case "Orlando":
            office = "MLB";
            gridX = 26;
            gridY = 68;
            break;
        case "Chicago":
            office = "LOT";
            gridX = 76;
            gridY = 73;
            break;        
        case "Washington":
            office = "LWX";
            gridX = 96;
            gridY = 72;
            break;
        case "Atlanta":
            office = "FFC";
            gridX = 51;
            gridY = 87;
            break;        
        case "Seattle":
            office = "SEW";
            gridX = 125;
            gridY = 68;
            break;
        case "San Francisco":
            office = "MTR";
            gridX = 85;
            gridY = 105;
            break;
        case "Los Angeles":
            office = "LOX";
            gridX = 155;
            gridY = 45;
            break;            
        default:
            console.log("City not found");
            return;
    }
    getWeather(office, gridX, gridY);
}

// Function to get weather for the user's current location
function getCurrentLocationWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            // Fetch office and grid position based on current latitude and longitude
            fetch('https://api.weather.gov/points/' + latitude + ',' + longitude)
                .then(function(response) {
                    return response.json();
                })
                .then(function(data) {
                    var office = data.properties.gridId;
                    var gridX = data.properties.gridX;
                    var gridY = data.properties.gridY;
                    getWeather(office, gridX, gridY);
                })
                .catch(function(error) {
                    console.log(error);
                });
        });
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

// Function to fetch weather data based on office and grid position
function getWeather(office, gridX, gridY) {
    var url = 'https://api.weather.gov/gridpoints/' + office + '/' + gridX + ',' + gridY + '/forecast';
    fetch(url)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            displayWeather(data);
        })
        .catch(function(error) {
            console.log(error);
        });
}

// Function to display weather information
function displayWeather(data) {
    var weatherInfo = document.getElementById('weather-info');
    weatherInfo.innerHTML = '';
    if (data.type === "Feature") {
        var period = data.properties.periods[0].name;
        var temperature = data.properties.periods[0].temperature;
        var humidity = data.properties.periods[0].relativeHumidity.value;
        var windSpeed = data.properties.periods[0].windSpeed;
        var direction = data.properties.periods[0].windDirection;
        var forecast = data.properties.periods[0].detailedForecast;
        var weatherHtml = '<h2>Weather Forecast for ' + period + '</h2>' +
            '<p>Temperature: ' + temperature + ' &#8451;</p>' +
            '<p>Humidity: ' + humidity + '%</p>' +
            '<p>Wind Speed: ' + windSpeed + ' m/s ' + direction + '</p>' +
            '<h3> Forecast </h3>' +
            '<p>' + forecast + '</p>';
        weatherInfo.innerHTML = weatherHtml;
    } else {
        weatherInfo.innerHTML = '<p>Failed to retrieve weather information.</p>';
    }
}
