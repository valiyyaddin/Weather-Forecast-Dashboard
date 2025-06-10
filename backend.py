import requests

API_KEY="b50c71c35370985a05337630b5ce83c7"

def get_data(place,forecast_days,kind = None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data=data['list']
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind =="Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        return  filtered_data
    if kind =="Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days=3, kind="Temperature"))