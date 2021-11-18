
class  Util:
    @staticmethod
    def parse_weather_data(response):
        latitude = response["coord"]['lat']
        longitude = response["coord"]['lon']
        humidity = response["main"]['humidity']
        pressure = response["main"]['pressure']
        temperature = response["main"]['temp']
        temp_max = response["main"]['temp_max']
        temp_min = response ["main"]['temp_min']
        visibility = response["visibility"]
        sunrise = response["sys"]['sunrise']
        sunset = response["sys"]['sunset']
        speed = response["wind"]['speed']
        
        data = {
            "latitude":latitude,
            "longitude":longitude,
            "humidity":humidity,
            "pressure":pressure,
            "temperature":temperature,
            "temp_max":temp_max,
            "temp_min":temp_min,
            "visibility":visibility,
            "sunrise":sunrise,
            "sunset":sunset,
            "speed":speed
            
            


        }

        return data


class  Climate:
    @staticmethod
    def parse_climate_data(get):
        # latitude = get["city"]['coord']['lat']
        # longitude = get["city"]['coord']['lon']
        day = get["list"]['temp']['day']
        min = get["list"]['temp']['min']
        max = get["list"]['temp']['max']
        night = get["list"]['temp']['night']
        eve = get["list"]['temp']['eve']
        morn = get["list"]['temp']['morn']

        
        climate_data = {
            # "latitude":latitude,
            # "longitude":longitude,
            "day":day,
            "min":min,
            "max":max,
            "night":night,
            "eve":eve,
            "morn":morn
            
        }
        
        return climate_data
