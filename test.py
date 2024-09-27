from flask import Flask
import requests
import json



app = Flask(__name__)

response = requests.get("https://api.weatherusa.net/feed?type=forecast&units=e&daily=0&maxtime=0h&q=39.726,-85.891&tz=US/Eastern")
response.raise_for_status()

jsonResponse = response.json()

@app.route("/temperature")
def temperature():

    return f'<p>In New Palestine, Indiana: the temperature is {jsonResponse[0]["temp"]} faherenheit</p>'

@app.route("/wind")
def wind():

    return f'<p>In New Palestine, Indiana: the wind speed is {jsonResponse[0]["wspd"]} miles per hour</p>'

@app.route("/weather")
def weather():

    return f'<p>In New Palestine, Indiana: the current weather is: {jsonResponse[0]["wx_str"]}</p>'

