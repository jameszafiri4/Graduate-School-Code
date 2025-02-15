'''
Simple API client program making a call using the NOAA forecast example from class.
The program relies on two functions, one being the API URL to retrieve data for
the inputted latitude and longitude by the user, and the other uses data from that
first call to receive more forecast data to present to the user from another API URL.
This was created based off of the National Weather Service API Web Service example for
TOP/31,80/ and 39.7456,-97.0892 (just was the initial testing, others examples work as well)
This code is written in Python and was tested on Visual Studio Code.
James Zafiri
version 1.0.0
Week 3 of CSC6304
'''

import requests

def get_forecast(office, gridX, gridY):
    '''
    This function will do the work of getting the forecast details of the location that
    is specified by the user by making an API URL call. It takes the 3 needed parameters
    (office, gridX, gridY) and will then return the temperature, trend(if applicable),
    and a short forecast. These are obtained by the get_location_forecast function.
    '''

    # Construct the API URL for the given office, gridX, and gridY based on latitude & longitude
    url = f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast'

    # Send a GET request to the API URL
    response = requests.get(url)
    # If the response is successful, extract the forecast data
    if response.ok:
        data = response.json()
        forecast = str(data['properties']['periods'][0]['temperature'])
        # some locations have null value for the trend, so we will check for that to not get error
        temperatureTrend = data['properties']['periods'][0]['temperatureTrend']
        if temperatureTrend is not None:
            forecast += "F " + temperatureTrend
        else:
            forecast += "F"
        forecast += " - " + data['properties']['periods'][0]['shortForecast']
        return forecast
    else:
        raise Exception('Failed to fetch forecast.')
    
def get_location_forecast(latitude, longitude):
    '''
    This function will obtain the user input parameters of latitude and longitude, and fetch
    that information by making an API call to the URL. It will ensure that the correct data
    is received for the location so we can retrieve the forecast for the user via prior function.
    '''

    # Construct the API URL for getting office, gridX, and gridY parameters based on latitude,longitude
    url = f'https://api.weather.gov/points/{latitude},{longitude}'

    # Send a GET request to the API URL
    response = requests.get(url)
    # If the response is successful, extract office, gridX, and gridY parameters
    if response.ok:
        data = response.json().get('properties', {})
        office = data.get('gridId', '')
        gridX = data.get('gridX', '')
        gridY = data.get('gridY', '')
        # Call get_forecast function to get the forecast for the location
        if office and gridX and gridY:
            forecast = get_forecast(office, gridX, gridY)
            return forecast
        else:
            raise Exception('Failed to fetch location data.')
    else:
        raise Exception('Failed to fetch location data.')

def main():
    '''
    This is our main function where we will interact with the user to obtain the
    latitude and longitude. We will use these values to obtain the location data,
    and then also retrieve forecast data based on the location.
    '''
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    
    try:
        forecast = get_location_forecast(latitude, longitude)
        print("Forecast:", forecast)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
