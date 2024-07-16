
import requests
from bs4 import BeautifulSoup
from timeParser import Speak

def get_weather():
	cookies = {
	    'ab_audience_2': '52',
	    '_ym_uid': '1698653589275841801',
	    '_ym_d': '1698653589',
	    'cityIP': '5164',
	    'cityUS': '5164',
	    '_gid': 'GA1.2.2122469497.1704012768',
	    '_ym_isad': '1',
	    '_ga': 'GA1.1.397224983.1698653589',
	    '_ga_B60LCM0EM3': 'GS1.1.1704015471.7.1.1704015852.33.0.0',
	    '_ga_1S104XLRYD': 'GS1.1.1704015462.3.1.1704015856.29.0.0',
	    '_ga_WYG41YMCJS': 'GS1.1.1704015462.3.1.1704015856.29.0.0',
	}

	headers = {
	    'authority': 'www.gismeteo.kz',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
	    'cache-control': 'max-age=0',
	    # 'cookie': 'ab_audience_2=52; _ym_uid=1698653589275841801; _ym_d=1698653589; cityIP=5164; cityUS=5164; _gid=GA1.2.2122469497.1704012768; _ym_isad=1; _ga=GA1.1.397224983.1698653589; _ga_B60LCM0EM3=GS1.1.1704015471.7.1.1704015852.33.0.0; _ga_1S104XLRYD=GS1.1.1704015462.3.1.1704015856.29.0.0; _ga_WYG41YMCJS=GS1.1.1704015462.3.1.1704015856.29.0.0',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}



	response = requests.get('https://www.gismeteo.kz/weather-astana-5164/now/', cookies=cookies, headers=headers)
	# print(response.text.find(class_="unit unit_temperature_c"))
	src = response.text
	# print(response.text)

	soup = BeautifulSoup (src, 'html.parser')

	# print(soup.find(class_='unit unit_temperature_c').text)
	Speak(soup.find(class_='unit unit_temperature_c').text)

# get_weather()

# with open('parse.html', 'w') as file:
	# file.write(response.text)