import requests
from bs4 import BeautifulSoup
from csv import writer
from coin import Coin
import datetime

time_begin = datetime.datetime.now()
URL = 'https://coinmarketcap.com/all/views/all/'
# URL = 'https://coinmarketcap.com/'
RESPONSE = requests.get(URL)
SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')
ROW = SOUP.findAll("tr")[1:]

with open('coin_data.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Rank", "Coin", "Symbol", "Market Cap", "Price"])

    rank = 1
    for elem in ROW:
        name = elem.find('a').find_next('a').get_text()
        symbol = elem.find('a').get_text()
        mcap = elem.find(class_="market-cap").get_text()
        price = elem.find(class_="price").get_text()

        coin = Coin(rank, name, symbol, mcap, price)

        csv_writer.writerow(coin.get_all_data())
        rank += 1
    
    time_end = datetime.datetime.now() - time_begin
    total_time = round(time_end.total_seconds(), 2)
    print(f"Time elapsed: {total_time} seconds")
        