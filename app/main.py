import requests


def get_weather() -> None:

    API_KEY = "b47adef0ac6d4d919b5131859253105"
    CITY = "Paris"

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=en"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Weather in {location}: {condition}, {temp}°C"
    else:
        return f"Mistake {response.status_code} - failed to retrieve data."


if __name__ == "__main__":
    print(get_weather())
