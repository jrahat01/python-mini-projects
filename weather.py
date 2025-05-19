#importing the requests library, letting the python file/app make HTTP requests (asking a website or API for data)
#if error occurs with requests, run 'pip install requests' in terminal then restart IDE
#im gonna load the requests module so I can use it to talk to websites
import requests

#python stores your API key in a variable called 'api_key' which is the pass to use the weather service
api_key = "247d6d424cd7a626fff7d70e58a4d82a"

#python saves the base address in a variable called 'base_url' of the weather API, where all the requests will go
base_url = "https://api.openweathermap.org/data/2.5/weather"


#Python now pauses asking and waiting for the user to type a city name, then stores it in a variable 'city'
city = input("Enter the name of the city: ")


#python is building the full URL that it is going to send to the weather website
request_url = f"{base_url}?q={city}&appid={api_key}&units=imperial"
#base_url main API address
#?q={city} is the city name
#&appid={api_key} is the API key
#&units=imperial is the unit of measurement (imperial for Fahrenheit) (metric for Celsius)


#python now sends a GET request to the API using the full URL and then saves the reply in a variable called 'response'
response = requests.get(request_url)

#now python will check "did the API respond with a 200 status code?" if yes then it continues inside the if block
#if not then it will skip down the the else block and print "An error occurred"
if response.status_code == 200: #when sending a request to an API(or any website), the status code will tell how the request went, 
#in this case 200 means it worked

    #python now turns the reply from the weather API (which is in JSON format) into a python dictionary then saves it in a variable called 'data'
    data = response.json() 
    #python now digs into the data dictionary and finds 'weather' list, taking the first item in that list, then pulls out the 'description'
    weather = data['weather'][0]['description']
    #data['weather'] is a list, getting the list
    #[0] is the first(and only) item in the dictionary list
    #['description'] pulls the actual weather description

    #Python grabs the 'main' dictionary in the JSON, then gets the 'temp' value from it
    temperature = data['main']['temp']
    #data['main'] is another dictionary
    #['temp'] gets the actual temperature

    #shows the weather description using an f-string to include variables
    #python prints the weather info into a sentence with the city name and prints the temperature in fahrenheit
    print(f"Weather in {city}: {weather}")
    print(f"Temperature in {city}: {temperature}°F")
#If the API didn't respond with 200 python will run this instead telling the user an error occured.
else:
    print("An error occurred, try again")




