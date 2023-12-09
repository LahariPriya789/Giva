import requests
from bs4 import BeautifulSoup

url = 'https://www.giva.co/?gclid=EAIaIQobChMIsOOUsOuzggMVzqRmAh1RIQ20EAAYASAAEgId__D_BwE'
response = requests.get(url)
# print(response)

page_source = response.content
jsoup = BeautifulSoup(page_source)
div1 = jsoup.find('div', attrs={'class':'collection_list'})
div2 = div1.find_all('div',attrs={'class':'collection_list_item'})

final_list = []
for div_items in div2:
    a = div_items.find('a')
    link = a['href']
    final_list.append(link)

if __name__ == '__main__':
    print(final_list)