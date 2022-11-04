from modules.collect import CollectData
from modules.date_time import GetTime
from csv import writer

import time

def get_coin_information(data):
    
    price = data.get_price()
    percent_price = data.get_price_percent()
    volume = data.get_volume()
    volume_percent = data.get_volume_percent()
    value_percent = data.get_value_compare_with_market_percent()
    lowest_price = data.get_lowest_price()
    highest_price = data.get_highest_price()

    return [price, percent_price, volume, volume_percent, value_percent, lowest_price, highest_price]

def add_row_csv(filename, lst):
    with open('datasets/' + filename, 'a', newline='') as f:
        writer_object = writer(f)
        writer_object.writerow(lst)
        f.close()

if __name__ == '__main__':
    

    filenames = [
        'bnb.csv',
        'bitcoin.csv'
        # 'eth.csv'
    ]

    links = [
        'https://coinmarketcap.com/th/currencies/bnb/',
        'https://coinmarketcap.com/th/currencies/bitcoin/'
        # 'https://coinmarketcap.com/th/currencies/ethereum/'
    ]

    while True:
        for i in range(len(links)):
            day, date, times = GetTime().get_time()
            data_ = CollectData(links[i])
            information = get_coin_information(data_)
            information = [day, date, times] + information 
            print(information)
            add_row_csv(f'{filenames[i]}', information)
        time.sleep(3)