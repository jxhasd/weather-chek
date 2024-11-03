import requests
from translate import Translator


# перевод города на англ
city = input()
translator = Translator(from_lang="russian", to_lang="english")
en_city = translator.translate(city)
print(en_city)


# Информация по координатам
api_url_с = "https://api.geoapify.com/v1/geocode"
apiKey_с = "<api>"
response_с = requests.get(f"{api_url_с}/search?city={en_city}&apiKey={apiKey_с}").json()
print(response_с)
lon = response_с["features"][0]["properties"]["lon"]
lat = response_с["features"][0]["properties"]["lat"]
print(lon, lat)


# информация по погоде
headers = {
    "x-rapidapi-key": "<api>",
    "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
}
url_w = "https://weatherapi-com.p.rapidapi.com/current.json"
querystring = {"q": f"{lat}, {lon}"}
response_w = requests.get(url_w, headers=headers, params=querystring).json()
print(response_w)

# перевод слов
translator1 = Translator(from_lang="english", to_lang="russian")
weather_en = response_w["current"]["condition"]["text"]
weather_ru = translator1.translate(weather_en)
location_city_en = response_w["location"]["name"]
location_city_ru = translator1.translate(location_city_en)
location_country_en = response_w["location"]["country"]
location_country_ru = translator1.translate(location_country_en)


# главное по погоде вывод
print()
print(f"Локация: {location_country_ru}, {location_city_ru}")
print("Дата:", response_w["current"]["last_updated"])
print("Температура:", response_w["current"]["temp_c"], "°C")
print("Погода:", weather_ru)
print("Ветер:", response_w["current"]["wind_kph"], "км/ч")
