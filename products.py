from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.centuryply.com/plywood/architect-plywood')
soup = BeautifulSoup(source.content, 'lxml')

main = soup.find('div',class_='desktopshowns')
img = main.find('div',class_='prodimgs text-center').img['src']
print(img)

p_name = main.find('div',class_='description-prod').p.strong.text
print(p_name)

p_desc = main.find('div',class_='description-prod').p.text.replace('\n','')
print(p_desc)

p_name_logo  = main.find('div',class_='left-logsars').img['src'].replace('..','https://www.centuryply.com/')
print(p_name_logo)

p_tags = main.find('div',class_='product-tags').text.replace('\n','')
print(p_tags)

p_warranty = main.find('div',class_='col-lg-6').div.label.span.text
print(p_warranty)