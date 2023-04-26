from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import os


source = requests.get('https://www.centuryply.com/centurylaminates/')
soup = BeautifulSoup(source.content, 'lxml')

l= []
for main in soup.select('li.dropdown-submenu'):
    for a_link in main.find_all('a'):
        try:
            t_link = a_link['href'].replace('#','')
            f_name = t_link.replace('.php','')
            m_link = f'https://www.centuryply.com/centurylaminates/{t_link}'
            l.append(m_link)

            # folder_location = f'./data/{f_name}'
            # if not os.path.exists(folder_location):
            #     os.mkdir(folder_location)

        except:
            print('')

t = list(set(l))
print(t)





for i in range (len(t)):
    print(f'>> {t[i]}')
    url = f'{t[i]}'
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')


    for src in soup.find_all('div',class_='product-meta'):
        links = src.a
        link =links.find_next('a')['href']
        link = f'https://www.centuryply.com/centurylaminates/{link}'
        #print(link)



        source = requests.get(link)
        soup = BeautifulSoup(source.content, 'lxml')
        print(f'>> {link}')

        img = soup.find('div',class_='product-img').a['bg-image']
        prod_img = f'https://www.centuryply.com/centurylaminates/{img}'
        print(prod_img)

        name = soup.find('div',class_='product-heading').h1.text
        print(name)
        
        f_name = name.replace(' ','_')
        filenames = f'./data/{f_name}.csv'
        with open(filenames , 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Prod_link','Name','Images', 'Prod_Desc'])


            p_name = soup.find('div',class_='product-heading').h1.text
            print(p_name)
            desc = soup.find('div',class_='product-description').p.text
            print(desc)

            csv_writer.writerow([link,p_name,prod_img,desc])
        print(csv_file.closed)