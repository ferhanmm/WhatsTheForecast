# Greets user via a form using POST and a layout
#import os
from flask import Flask, render_template, request
from helpers import lookup

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    #testNum = os.environ.get("testNum")
    return render_template("greet.html", name=request.form.get("name"))
    #return render_template("greet.html", name=testNum)




@app.route("/weather", methods=["GET", "POST"])
#@login_required
def weather():
    #"""Get stock quote."""
    # check if post
    if request.method == "POST":
        # get the symbol from user and check
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must provide Symbol")
        # check if stock symbol exists in api call using the lookup

        code = lookup(symbol)

        # if stockSymbol == None:
        #    return apology("Symbol doesn't exist")
        # get the symbol, name, and price and render the result page
        return render_template("weather.html", location = code["location"], temp = code["temp"], 0dateDate = code["0dateDate"])

# create results page
    # if get, go to quote page
    else:
        return render_template("quote.html")


