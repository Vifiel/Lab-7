import requests

#Latitude and longitude of Perm
LAT = 58.01
LON = 56.25
APIID = "cd656b36d2ffa460c03eeca1debe70a3"


response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={APIID}")


data = response.json()


print("Weather in Perm city")
print(f"Mainly {data['weather'][0]['main']}")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Air pressure: {data['main']['pressure']} hPa")
