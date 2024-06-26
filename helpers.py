import os, requests

from flask import redirect, render_template, request, session
from markupsafe import Markup
from functools import wraps

def iplookup(ip_addr):

    # Contact API
    try:
        url = f"http://ipwho.is/{ip_addr}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        ip = response.json()
        return {
            "city": ip['city'],
            "region": ip['region_code']
            }
    
    except (KeyError, TypeError, ValueError):
        return None

def lookup(symbol):

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={symbol}&days=10&aqi=yes&alerts=no"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        weather = response.json()
        return {
            "fullWeather": weather,
            "location": weather['location']['name'],
            "temp": weather['current']['temp_f'],
            "zerodayDate": weather['forecast']['forecastday'][0]['date'],
            "zerodayHigh": weather['forecast']['forecastday'][0]['day']['maxtemp_f'],
            "onedayDate": weather['forecast']['forecastday'][1]['date'],
            "onedayHigh": weather['forecast']['forecastday'][1]['day']['maxtemp_f'],
            "twodayDate": weather['forecast']['forecastday'][2]['date'],
            "twodayHigh": weather['forecast']['forecastday'][2]['day']['maxtemp_f']
            }
    
    except (KeyError, TypeError, ValueError):
        return None

def apology():
    svg = open('./static/logo.svg').read()

    return render_template("apology.html",logo=Markup(svg))