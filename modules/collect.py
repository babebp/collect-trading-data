import bs4
import requests


class CollectData:
    def __init__(self, link):
        self.link = link
        data = requests.get(self.link)
        self.soup = bs4.BeautifulSoup(data.text)
        

    def get_price(self):
        price = self.soup.find('div', {'class': 'priceValue'})  
        data = price.find('span')
        return float(data.text[1::].replace(',', ''))

    def get_price_percent(self):
        percent_updown = self.soup.find('div', {'class': 'sc-1prm8qw-0 cyZVgY priceTitle'})
        data = percent_updown.find('span', {'class': 'sc-15yy2pl-0 gEePkg'})
        
        if data.find('span', {'class': 'icon-Caret-down'}):
            return float(data.text[:-1].replace(',', '')) * - 1
        elif data.find('span', {'class': 'icon-Caret-up'}):
            return float(data.text[:-1].replace(',', '')) 

    def get_value_compare_with_market_percent(self):
        value_compare_with_market_percent = self.soup.find_all('div', {'class': 'statsItemRight'})  
        data = value_compare_with_market_percent[0].find('span', {'class': 'u2x6b4-0 chbrcp'})

        if data.find('span', {'class': 'icon-Caret-down'}):
            return float(data.text[:-1].replace(',', '')) * - 1
        elif data.find('span', {'class': 'icon-Caret-up'}):     
            return float(data.text[:-1].replace(',', '')) 

    def get_volume(self):
        volume = self.soup.find_all('div', {'class': 'statsItemRight'})  
        data = volume[2].find('div', {'class': 'statsValue'})
        return float(data.text[1::].replace(',', ''))

    def get_volume_percent(self):
        volume_percent = self.soup.find_all('div', {'class': 'statsItemRight'})  
        data = volume_percent[2].find('span', {'class': 'u2x6b4-0 chbrcp'})

        if data.find('span', {'class': 'icon-Caret-down'}):
            return float(data.text[:-1].replace(',', '')) * - 1
        elif data.find('span', {'class': 'icon-Caret-up'}):
            return float(data.text[:-1].replace(',', '')) 
        

    def get_lowest_price(self):
        lowest_price = self.soup.find('div', {'class': 'sc-1prm8qw-0 fCbTtB'})  
        data = lowest_price.find('span', {'class': 'n78udj-5 dBJPYV'})
        return float(data.text[1::].replace(',', ''))

    def get_highest_price(self):
        highest_price = self.soup.find('div', {'class': 'sc-1prm8qw-0 gtqyUe'})  
        data = highest_price.find('span', {'class': 'n78udj-5 dBJPYV'})
        return float(data.text[1::].replace(',', ''))