from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.centuryply.com/centurylaminates/single.php?productid=1321')
soup = BeautifulSoup(source.content, 'lxml')

img = soup.find('div',class_='product-img').a['bg-image']
prod_img = f'https://www.centuryply.com/centurylaminates/{img}'
print(prod_img)

name = soup.find('div',class_='product-heading').h1.text
print(name)

desc = soup.find('div',class_='product-description').p.text
print(desc)