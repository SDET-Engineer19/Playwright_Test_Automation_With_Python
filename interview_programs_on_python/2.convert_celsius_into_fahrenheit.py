def get_fahrenheit_into_celsius(celsius_val):
    fahrenheit_val = (celsius_val * 1.8) + 32
    return fahrenheit_val


class Celsius_Into_Fahrenheit:
    fahrenheit_val = get_fahrenheit_into_celsius(40)
    print(fahrenheit_val)
