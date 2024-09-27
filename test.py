from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather():
    response = requests.get("https://api.weatherusa.net/feed?type=forecast&units=e&daily=0&maxtime=0h&q=39.726,-85.891&tz=US/Eastern")

    if response.status_code == 200:
        return response.json()
    else:
        return None

weather_data = get_weather()

@app.route("/")
def index():
    return render_template('index.html',day=weather_data[0]["day_name"])

@app.route("/temperature")
def temperature():
    return render_template('temperature.html',temperature=weather_data[0]["temp"])

@app.route("/wind")
def wind():
    return render_template('wind.html',wind=weather_data[0]["wspd"])

@app.route("/weather")
def weather():
    return render_template('weather.html',weather=weather_data[0]["wx_str"])
   

