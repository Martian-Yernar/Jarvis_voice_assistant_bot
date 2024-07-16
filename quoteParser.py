import requests
from bs4 import BeautifulSoup
import random
from timeParser import Speak

def Quotes(genre):
    headers = {
        'authority': 'quotes.toscrape.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-GB;q=0.6',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    }

    # response = requests.get('https://quotes.toscrape.com', headers=headers)
    # src = response.text
    # soup = BeautifulSoup(src, 'html.parser')
    # tags = soup.find('div', class_='col-md-4 tags-box').find_all('a', class_='tag')

    # for tag in tags:
    #     print(f'{tag.text} /', end=' ')
    # print(' ')
    # genre = input('Write the genre: ')

    response = requests.get(f'https://quotes.toscrape.com/tag/{genre}/', headers=headers)
    src = response.text
    soup = BeautifulSoup(src, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # for quote in quotes:
    #     print(quote.text)

    # for author in authors:
    #     print(author.text)
    # print(' ')

    n = random.randint(0, len(quotes)-1)
    # print(n)
    Speak(f'{quotes[n].text} \n by {authors[n].text}')

    # for i in range(len(quotes)):
    #     print(f'{quotes[i].text} \n by {authors[i].text}')
    #     print(' ')


# with open('index_selenium.html', 'w') as file:
#     file.write(response.text)