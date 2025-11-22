#5 DAY WEATHER FORECAST

import requests

API_KEY ="861646fa193ea5f689ec7da28df240cf"

def get_5day_forecast(city):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = { "q": city, "appid": API_KEY, "units" : "metric" }

    response = requests.get(base_url, params=params)
    data = response.json()

    if str(data.get("cod")) != "200" :
         print("Try again. Invalid city name.")
         return

    print(f"\n 5-Day Forecast for {city.title()}:\n")


    for entry in data["list"][::8]:
        date = entry["dt_txt"].split(" ")[0]
        desc = entry["weather"][0]["description"].title()
        temp = entry["main"]["temp"]
        print(f"{date}: {temp}\u00B0C - {desc}")


city = input("Enter city name: ")
get_5day_forecast(city)
