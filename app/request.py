
import urllib.request,json
from .models import Weather


# Getting api key
api_key = None
# Getting the weather base url
base_url = None
def configure_request(app):
    global api_key,base_url
    api_key = app.config['WEATHER_API_KEY']
    base_url = app.config['WEATHER_API_BASE_URL']



def get_weather(location):
    '''
    Function that gets the json response to our url request
    '''
    get_weather_url = base_url.format(location, api_key)
    

    with urllib.request.urlopen(get_weather_url) as url:
        get_weather_data = url.read()
        get_weather_response = json.loads(get_weather_data)

        weather_results = None

        if get_weather_response['results']:
            weather_results_list = get_weather_response['results']
            weather_results = process_results(weather_results_list)
            
    print(weather_results)


    return weather_results

def process_results(weather_list):
    '''
    Function  that processes the weather result and transform them to a list of Objects

    Args:
        weather_list: A list of dictionaries that contain weather details

    Returns :
        weather_results: A list of weather objects
    '''
    weather_results = []
    for weather_item in weather_list:
        coordinates = weather_item.get('coordinates')
        weather = weather_item.get('weather')
        main= weather_item.get('main')
        visibility = weather_item.get('visibility')
        
        
    if coordinates:
            weather_object = Weather(coordinates,weather,main,visibility)
            weather_results.append(weather_object)


    return weather_results
def search_city(city_name):
    search_city_url = 'https://api.openweathermap.org/data/2.5/weather?appid={}&query={}'.format(api_key,city_name)
    with urllib.request.urlopen(search_city_url) as url:
        search_city_data = url.read()
        search_city_response = json.loads(search_city_data)
        search_city_results = None
        if search_city_response['results']:
            search_city_list = search_city_response['results']
            search_city_results = process_results(search_city_list)
    return search_city_results

