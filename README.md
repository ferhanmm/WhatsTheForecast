# What's the forecast
#### Video Demo:  <URL HERE>
#### Description:
    This is our CS50x final project, it's a simple and fast way to get current weather info and forecast. You can visit the site using the link below: 
    https://whatstheforecast.com

0. **Developers**
    -   Ferhan Moton
    -   Mazen Almontheri
1. **Hosting**
   - Domain name
        -   We chose this domain name to improve search engine optimization, and its easier to remember. We purchased the domain from Google Domains.

   - Server hosting
        -   We Chose Digital Ocean for its simplicity and enhanced performance, and the ability to manage through GitHub. Also the ability to store API keys in the environment file.

2.  **Flask** - We chose Flask as the framework for our project because it's easy to get started and we took advantage of the material from Week 9 to help us along the way. 

    - app.py
        - Our app.py file contains two routes: 
            - The default (/) route allows the user to see their weather based on the IP address from the visitors HTTP header. It grabs the IP address and provides it to a function in helpers.py to initiate an API request.
            - The weather route allows the user to lookup weather for a specific location. It grabs the search location and provides it to a function in helpers.py to initiate an API request.
            - app.py also opens the logo SVG and renders it to be used in HTML
    - helpers.py
        - helpers.py contains 3 functions:
            - iplookup function takes the ip address input and sends the request to weatherapi.com, then returns the forecast data.
            - lookup function takes the search location input and sends the request to weatherapi.com, then returns the forecast data.
            - apology function is triggered when weatherapi.com is unable to determine the location based on the user input. This function renders apology.html.

    - HTML pages
        - Layout
            - Is the main template used throughout the website. It includes the CSS customizations and Bootstrap references.
        - index
            - This is the default page that is rendered for a visitor. Uses the data returned from iplookup function to display the forecast information in a container layout.
        - Weather
            - This is page that is rendered for a visitor when they use the search feature. Uses the data returned from lookup function to display the forecast information in a container layout.
        - apology
            - This is the error page that is rendered for a visitor when the API is unable to determine the location. 
    - Static files
        - logo.svg is the site logo and is opened by app.py and rendered for layout.html
        - water.png is used in the index.html and weather.html pages to display the chance of rain.
3. **WeatherAPI**
    -   We decided on WeatherAPI.com as it has a free plan that includes all weather data for today, tomorrow and after tomorrow. We may expand in the future to include more data.
    https://www.weatherapi.com/api-explorer.aspx
   -    Another good feature is the ability to grab user's IP address from the browser data in order to determine and immediately provide the visitor with weather data.
    http://api.weatherapi.com/v1/ip.json?key={api_key}&q={ip_addr}
    
4. **GitHub**
    -   We used GitHub to collaborate project development, we have connected our hosting server with GitHub to automate code deployment and push updates.
    -   We have installed GitHub desktop and linked it with our account to fetch new code and push changes.
    -   This feature has added so much value to our project as it streamlines development and it cut down 
