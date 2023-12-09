import requests
from bs4 import BeautifulSoup
from for_giva import final_list
import pandas as pd
import re

result_list = []
for i,links in enumerate(final_list):
    urls = 'https://www.giva.co/'+links
    resp = requests.get(urls)
    # print(resp)

    jsoup = BeautifulSoup(resp.content)
    ul = jsoup.find('ul', attrs={'data-sectionid':"collection-template"})
    li = ul.find_all('li', attrs={'class':'grid__item grid__item--collection-template small--one-half medium-up--one-quarter'})
    # print(li)

    for lis in li:
        dummy = dict()
        div = lis.find('div', attrs ={'class':'grid-view-item product-card'})
        try:
            a = div.find('div', attrs={'class':'h4 grid-view-item__title product-card__title'})
            if a:
                name = a.text
                dummy['Item Name'] = name

        except:
            pass

        span = lis.find('span', attrs={'class':'price-item price-item--sale'})
        price = span.text
        dummy['Sale Price'] = price

        span2 = lis.find('span', attrs={'class':'price-item price-item--regular'})
        reg_price = span2.text
        cleaned_price = re.sub(r'\s+', ' ', reg_price).strip()
        ori_price = cleaned_price.split(' ')[-1]
        # print(ori_price)
        dummy['Original Price'] = ori_price
        dummy['category'] = i+1

        result_list.append(dummy)

# print(result_list)
df = pd.DataFrame(result_list)
# # print(df)
df.to_csv('D:\\$PYTHON\\ Giva jewel.csv', index=False)