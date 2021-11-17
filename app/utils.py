class  Util:
    @staticmethod
    def parse_weather_data(response):
        latitude = response["coord"]['lat']
        longitude = response["coord"]['lon']
        humidity = response["main"]['humidity']
        pressure = response["main"]['pressure']
        temperature = response["main"]['temp']

        data = {
            "latitude":latitude,
            "longitude":longitude,
            "humidity":humidity,
            "pressure":pressure,
            "temperature":temperature
        }
        
        return data
