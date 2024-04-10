import requests


url = "https://api.openweathermap.org/data/2.5/weather?lat=39.6753592&lon=-104.783926&appid={apikey}"
response = requests.get(url)
if response.status_code == 200:
    d = response.json()
    print(d)
    print(f"The temperature is {d['main']['temp']} Kelvin")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


