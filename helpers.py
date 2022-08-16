import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def lookup(symbol):
    
    #"""Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={symbol}&aqi=yes"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        weather = response.json()
        return {
            "location": weather['location']['name'],
            "temp": weather['current']['temp_f']
            }
    
    except (KeyError, TypeError, ValueError):
        return None

    
    

 # http://api.weatherapi.com/v1/current.json?key={api_key}&q=(symbol)

