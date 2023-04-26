from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.centuryply.com/zykron-fibre-cement-board')
soup = BeautifulSoup(source.content, 'lxml')
l = []
main = soup.find('div',class_='product-listsection')
for src in soup.find_all('div',class_='desktopshowns'):
    for link in src.find_all('div',class_='cta-varioussets'):
        prod_link = link.a['href']
        #print(prod_link)
        l.append(prod_link)
    
print((l))