def get_weather_report(temp, humidity):

    if temp >= 30 and humidity >= 90:
        print("Weather is Hot and Humid ")
    elif temp >= 30 and humidity < 90:
        print("Weather is Hot ")
    elif temp < 30 and humidity >= 90:
        print("Weather is Cool and Humid")
    elif temp < 30 and humidity < 90:
        print("Weather is Cool ")
    else:
        print("Please Provide Exact Value For Temperature and Humidity")


class Weather_Report:
    temp = int(input("Enter Temperature Value : "))
    humidity = int(input("Enter Humidity Value : "))

    get_weather_report(temp, humidity)