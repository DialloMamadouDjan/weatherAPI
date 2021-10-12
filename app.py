import os
import requests
from flask import Flask, render_template, request, jsonify
import json
import datetime
from random import *



app = Flask(__name__)


@app.route('/api/weather/<city>', methods=['GET', 'POST'])
def citySearch(city):
    response = {}
    weatherUrl = "https://www.metaweather.com/api/location/search/?query="
    query = weatherUrl+city
    data = requests.get(query).json()
    if len(data) > 0:
        codeWoeid = []
        for item in data:
            codeWoeid.append(item['woeid'])
        id = str(codeWoeid[0])
        api = f'https://www.metaweather.com/api/location/{id}'
        dataWeather = requests.get(api).json()
        cityWeather = dataWeather['consolidated_weather']
        keys_to_remove = ['min_temp', 'wind_direction', 'air_pressure', 'visibility', 'predictability',
                    'humidity', 'wind_speed', 'id', 'created', 'wind_direction_compass', 'weather_state_abbr', 'max_temp']
        for key in keys_to_remove:
            for i in range(len(cityWeather)):
                cityWeather[i]['the_temp'] =int(cityWeather[i]['the_temp'])
                cityWeather[i]['the_temp'] =str(cityWeather[i]['the_temp'])
                del cityWeather[i][key]

                if (cityWeather[i]['weather_state_name'] == "Showers" or
                cityWeather[i]['weather_state_name'] == "Heavy Rain" or 
                cityWeather[i]['weather_state_name'] == "Light Rain" or 
                cityWeather[i]['weather_state_name'] == "Heavy Cloud") :

                    link = "https://random.dog/woof.json"
                    # link = requests.get(api).json()
                    # link = link["url"]

                elif (cityWeather[i]['weather_state_name'] == "Sunny" or
                cityWeather[i]['weather_state_name'] ==  "Light Cloud" or 
                cityWeather[i]['weather_state_name'] == "Clear"
                ):
                    link = "https://aws.random.cat/meow"
                    # link = requests.get(link)).json()
                    # link = link["file"]

                else :
                    link = "https://shibe.online/"

                cityWeather[i]["picture_weather"] = link
                cityWeather[i]['picture_weather'] = link
        for i in range(len(cityWeather)) :
            cityWeather[i]['applicable_date'] 
            _date = cityWeather[i]['applicable_date']
            _date = datetime.datetime.strptime(_date, '%Y-%m-%d')
            _date= ('{0}-{1}-{2:02}'.format(_date.month, _date.day, _date.year))
            _date= cityWeather[i]['weather_state_name']
            _date= cityWeather[i]['the_temp']


            del cityWeather[i]['applicable_date']
            del cityWeather[i]['weather_state_name']
            del cityWeather[i]['the_temp']
            cityWeather[i]['Day'] = _date
            cityWeather[i]['weather'] = _date
            cityWeather[i]['temperature'] = _date

        response["content"] = cityWeather
        return jsonify(response)
    else :
        valueFalse = {
    "content": [],
    "error": {
    "msg":"Town not found",
    "uid_error": "4"
        }
        }
        return jsonify(valueFalse)



if __name__ == '__main__':
    app.run(debug=True)
