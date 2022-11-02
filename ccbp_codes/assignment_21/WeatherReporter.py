#WeatherReporter

def get_weather_report(temperature):
    if temperature < 22:
        return "Cold"
    elif temperature >= 22 and temperature < 35:
        return "Warm"
    elif temperature >= 35:
        return "Hot"


temperature = int(input())
result = get_weather_report(temperature)
print(result)
