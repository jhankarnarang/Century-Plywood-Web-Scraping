from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


source = requests.get('https://www.centuryply.com/centurylaminates/')
soup = BeautifulSoup(source.content, 'lxml')

l= []
for main in soup.select('li.dropdown-submenu'):
    for a_link in main.find_all('a'):
        try:
            t_link = a_link['href'].replace('#','')
            m_link = f'https://www.centuryply.com/centurylaminates/{t_link}'
            l.append(m_link)
        except:
            print('')

t = list(set(l))
print(len(t))
listToStr = ' '.join([str(elem) for elem in t])
  
print(listToStr) 