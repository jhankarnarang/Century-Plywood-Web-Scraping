from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.centuryply.com/centurylaminates/urban-stitch.php')
soup = BeautifulSoup(source.content, 'lxml')


for src in soup.find_all('div',class_='product-meta'):
    links = src.a
    link =links.find_next('a')['href']
    link = f'https://www.centuryply.com/centurylaminates/{link}'
    print(link)