
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



def get_weather(category):
    '''
    Function that gets the json response to our url request
    '''
    get_weather_url = base_url.format('api_key')

    with urllib.request.urlopen(get_weather_url) as url:
        get_weather_data = url.read()
        get_weather_response = json.loads(get_weather_data)

        weather_results = None

        if get_weather_response['results']:
            weather_results_list = get_weather_response['results']
            weather_results = process_results(weather_results_list)


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
        latitude = weather_item.get('latitude')
        longitude = weather_item.get('longitude')
        country= weather_item.get('country')
        locality = weather_item.get('locality')
        region = weather_item.get('region')
        street= weather_item.get('street')
        
    if latitude:
            weather_object = Weather(latitude,longitude,country,locality,region,street)
            weather_results.append(weather_object)


    return weather_results

