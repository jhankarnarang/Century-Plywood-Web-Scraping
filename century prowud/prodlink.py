from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.centuryprowud.com/')
soup = BeautifulSoup(source.content, 'lxml')

main = soup.find_all('li')
print(main)