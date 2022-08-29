# Greets user via a form using POST and a layout
#import os
import imp
from flask import Flask, render_template, request, Markup, jsonify, redirect
from helpers import lookup, iplookup
from datetime import date, datetime
import calendar

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        dayofWeek = calendar.day_name[(date.today()).weekday()]
        dateCurrent = (date.today()).strftime("%m/%d/%y")
        svg = open('./static/logo.svg').read()
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip_addr = request.environ['REMOTE_ADDR']
        else:
            ip_addr = request.environ['HTTP_X_FORWARDED_FOR']

        if ip_addr == "127.0.0.1":
            ip_addr = "99.61.181.42" 

        locationcheck = iplookup(ip_addr)
        city=locationcheck["city"]
        region=locationcheck["region"]

        defaultWeather = lookup("{},{}".format(city, region))

        return render_template("index.html", logo=Markup(svg), weather = defaultWeather, weekday = dayofWeek, currentDate = dateCurrent)

    else:
        return render_template("index.html")


@app.route("/weather", methods=["GET", "POST"])
#@login_required
def weather():
   
    # check if POST
    svg = open('./static/logo.svg').read()
    if request.method == "POST":
        
        # get the symbol from user and check
        symbol = request.form.get("symbol")
       # if not symbol:
          #  return apology("Must provide Symbol")
        # check if stock symbol exists in api call using the lookup

        code = lookup(symbol)

        # if stockSymbol == None:
        #    return apology("Symbol doesn't exist")
        # get the symbol, name, and price and render the result page
        return render_template("weather.html", logo=Markup(svg), location = code["location"], temp = code["temp"], zerodayDate = code["zerodayDate"], zerodayHigh = code["zerodayHigh"], onedayDate = code["onedayDate"], onedayHigh = code["onedayHigh"], twodayDate = code["twodayDate"], twodayHigh = code["twodayHigh"])


    # if GET, go to quote page
    else:
        return redirect ("/")


