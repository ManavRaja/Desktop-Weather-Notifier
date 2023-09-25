# Desktop-Weather-Notifier
This is a Python script I wrote to send a desktop notification about the current weather in a specified location utilizing the <a href="https://openweathermap.org/">Open Weather Map API</a>. I have the script set to run every time I login to my laptop.

# How to use?
<ol>
  <li>Get an API Key from <a href="https://openweathermap.org/">Open Weather Map</a></li>
  <li>Clone this repository</li>
  <li>Create a ".env" file in the project directory, create 3 variables in it...</li>
  <ul>
    <li>"OPEN_WEATHER_API_KEY" and set it equal to your API Key</li>
    <li>"LATITUDE" and set it equal to the latitude of the location you want the weather data for</li>
    <li>"LONGITUDE" and set it equal to the longitude of the location you want the weather data for</li>
  </ul>
  <li>Create a Python Virtual Environment in the project directory, activate it, and run "pip install -r requirements.txt" to install the dependencies</li>
  <li>Run the "main.py" file with the virtual environment</li>
</ol>
