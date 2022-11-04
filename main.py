import time

from csv import writer
from modules.date_time import GetTime
from modules.collect import CollectData
from list_data import links_list as links, filenames_list as filenames

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
    while True:
        for i in range(len(links)):
            day, date, times = GetTime().get_time()
            data_ = CollectData(links[i])
            information = get_coin_information(data_)
            information = [day, date, times] + information 
            add_row_csv(f'{filenames[i]}', information)
        time.sleep(15)