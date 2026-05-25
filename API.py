""" Requests module providing access to websites or API's """
import requests # requests module used to access a web page and print the response text

# Ask user for the city's name
city = input("City Name: ")

# Enter your API key (for some API's you need to sign up and receive a key)
API_KEY = "your-api-key-goes-here"

# Generate the URL you will be requesting (read the documentation on the API site)
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# Use the request module function to get the data from that URL in JSON format
# JSON = javascript object notation. The other option is to get it as XML
# but JSON is sometimes easier to use right away.
json_data = requests.get(URL, timeout=10).json()

# If you view the full JSON data, you will see various dictionaries and lists you can access.
# Here we will only access the main description of the weather from the data coming back.
forecast = json_data['weather'][0]['description']

temp_k = json_data['main']['feels_like'] # Temperature in Kelvin
temp_c = temp_k - 273.15 # Converted to Celsius
temp_c = round(temp_c, 1) # Rounded to 1 decimal place

# Print the weather description.
# View the entire JSON return using a viewer such as https://codebeautify.org/jsonviewer
print(f"Forecast: {forecast}\nFeels Like: {temp_c}°C")