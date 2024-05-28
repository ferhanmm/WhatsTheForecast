import calendar
from flask import Flask, render_template, request, jsonify, redirect
from markupsafe import Markup
from helpers import lookup, iplookup, apology
from datetime import date, datetime, timedelta


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":

        dayofWeek = calendar.day_name[(date.today()).weekday()]
        dateCurrent = (date.today()).strftime("%m/%d/%y")
        dateToday = (date.today()).strftime("%m/%d")
        dateTomorrow = (date.today() + timedelta(1)).strftime("%m/%d")
        dateAfterTomorrow = (date.today() + timedelta(2)).strftime("%m/%d")

        svg = open('./static/logo.svg').read()
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip_addr = request.environ['REMOTE_ADDR']
        else:
            ip_addr = request.environ['HTTP_X_FORWARDED_FOR'].split(',')[0]

        if ip_addr == "127.0.0.1":
            ip_addr = "99.61.181.42" 

        locationcheck = iplookup(ip_addr)
        print(f"request.environ: {request.environ}")
        print(f"HTTP_X_FORWARDED_FOR: {request.environ.get('HTTP_X_FORWARDED_FOR')}")
        print(f"REMOTE_ADDR: {request.environ['REMOTE_ADDR']}")
        print(f"{ip_addr}: {locationcheck}")
        city=locationcheck["city"]
        region=locationcheck["region"]

        

        defaultWeather = lookup("{},{}".format(city, region))

        return render_template("index.html", logo=Markup(svg), weather = defaultWeather, weekday = dayofWeek, currentDate = dateCurrent, dateToday = dateToday, dateTomorrow = dateTomorrow, dateAfterTomorrow = dateAfterTomorrow)

    else:
        return render_template("index.html")


@app.route("/weather", methods=["GET", "POST"])
#@login_required
def weather():
   
    # check if POST
    dayofWeek = calendar.day_name[(date.today()).weekday()]
    dateCurrent = (date.today()).strftime("%m/%d/%y")
    dateToday = (date.today()).strftime("%m/%d")
    dateTomorrow = (date.today() + timedelta(1)).strftime("%m/%d")
    dateAfterTomorrow = (date.today() + timedelta(2)).strftime("%m/%d")
    svg = open('./static/logo.svg').read()
    if request.method == "POST":
        
        # get the symbol from user and check
        symbol = request.form.get("symbol")

        defaultWeather = lookup(symbol)

        if not defaultWeather:
            return apology()
        if defaultWeather == None:
            return apology()

        return render_template("weather.html", logo=Markup(svg), weather = defaultWeather, weekday = dayofWeek, currentDate = dateCurrent, dateToday = dateToday, dateTomorrow = dateTomorrow, dateAfterTomorrow = dateAfterTomorrow)


    # if GET, go to quote page
    else:
        return redirect ("/")



