import requests
import json
import pyttsx3
# from bot import city_name
# from bot import Speak
# from pprint import pprint


TOKEN = '302cd93571f7e72c3dba77940967b189'
# city_name = input("Input the city: ")
# city_name = "Astana"

def Speak(text):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate+10)
    engine.say(text)
    print(text)
    engine.runAndWait()

def get_weather(city_name, TOKEN):
    try:
        converter = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={TOKEN}")
        jsconv = converter.json()
        if len(jsconv) > 0:
            data = jsconv[0]
            _lat = data['lat']
            _lon = data['lon']
                
            weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={_lat}&lon={_lon}&appid={TOKEN}&units=metric")
            weatherconv = weather.json()
            _temp = weatherconv['main']['temp']
            cityName = weatherconv['name']
            Speak(f'Currently, it is {str(int(round(_temp, 0)))}°C in the {cityName}')
        else:
            Speak("Wrong name for the city, sir!")
            
    except Exception as ex:
        print(ex)
        Speak("Wrong name for the city, sir!")





