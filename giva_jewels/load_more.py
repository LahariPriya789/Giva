
import requests
from bs4 import BeautifulSoup

class Giva_jewel():
    def __init__(self):
        self.base_url = 'https://www.giva.co/collections/pendants?page='

    def giva(self,pg_num):
        title = []
        url = self.base_url+str(pg_num)
        response = requests.get(url)
        response.raise_for_status()

        jsoup = BeautifulSoup(response.content, 'html.parser')
        ul = jsoup.find('ul', attrs={'data-sectionid': "collection-template"})
        if ul is None:
            return title
        li = ul.find_all('li', attrs={
            'class': 'grid__item grid__item--collection-template small--one-half medium-up--one-quarter'})
        # print(li)

        for lis in li:
            dummy = dict()
            div = lis.find('div', attrs={'class': 'grid-view-item product-card'})
            try:
                a = div.find('div', attrs={'class': 'h4 grid-view-item__title product-card__title'})
                name = a.text
                dummy['Item Name'] = name
            except:
                pass

            title.append(dummy)
        return title

if __name__ == '__main__':
    obj = Giva_jewel()
    title = []
    page_no = 1
    while True:
        print('Page number: ', page_no)
        result = obj.giva(page_no)
        if result:
            title.extend(result)
            page_no = page_no + 1
        else:
            break

    print(title)
    print(len(title))
