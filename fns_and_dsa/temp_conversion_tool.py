FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

user_input = int(input("Enter the temperature to convert: "))
temp_input = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

if temp_input == f:
    convert_to_celsius(user_input)
elif temp_input == c:
    convert_to_fahrenheit(user_input)
else:
    print("Invalid temperature. Please enter a numeric value.")


def convert_to_celsius(fahrenheit):
    converted_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{user_input}°F is {converted_temp}°C")


def convert_to_fahrenheit(celsius):
    converted_temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{user_input}°C is {converted_temp}°F")
