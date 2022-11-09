import requests
import json
import os
from datetime import date
from datetime import datetime



##########################################################################
# This function consist in calling openweather API. It also prints the
# desired result.
##########################################################################

def handle_api_key():
    api_key=os.getenv('OpenWeatherMap_Key')
    if api_key:
        return api_key
    else:
        print ("No OpenWeatherMap Api Key found for this machine")
        api_key = input("Type in your api key or write exit to close this app:")

        if api_key == "exit":
            api_key = None
            print ("Closing app... Godbye!")
        else:
            # If the script is run as administrator this line will save the api key as environmental variable so it will be ready the next time
            os.environ['OpenWeatherMap_Key'] = str(api_key)

        return api_key

def call(cronologicalTime,location,days=1,units='metric'):
    api_key = handle_api_key()

    if api_key:
        # Preparing some variables
        [city, code]=location.split(',')
        location.replace(' ','+')
        if (units=='metric'):
            degrees=' ºC'
        else:
            degrees=' ºF'


        # Current weather case
        if (cronologicalTime=='current'):

            # Calling the API
            url='https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(location,units,api_key)
            response=requests.get(url)
            y=json.loads(response.content)

            if response.status_code != 200:
                print ('> ERROR: ' + y["message"])
            else:
                # Printing the result
                print(city + ' ('+ code + ') \n'+ datetime.strftime(date.today(),'%b %d, %Y'))
                print('> Weather: ' + y['weather'][0]['main'])
                print('> Temperature: ' + str(y['main']['temp']) + degrees)

        # Forecast weather case
        elif (cronologicalTime=='forecast'):

            # Building the url and calling the API
            url="https://api.openweathermap.org/data/2.5/forecast?q={}&units={}&cnt={}&appid={}".format(location,units,str((days+1)*8),api_key)
            response=requests.get(url)
            y=json.loads(response.content)

            if response.status_code != 200:
                print ('> ERROR: ' + y["message"])


            # Printing the result
            print(city + ' ('+ code + ')')
            indices=[8,16,24,32,39]
            for i in indices[0:days]:
                correspondingDate=datetime.strptime(y['list'][i]['dt_txt'][0:10],'%Y-%m-%d')
                print(datetime.strftime(correspondingDate,'%b %d, %Y'))
                print('> Weather: '+y['list'][i]['weather'][0]['main']+'.')
                print('> Temperature: '+ str(y['list'][i]['main']['temp']) +degrees)
