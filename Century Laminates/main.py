from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import os


source = requests.get('https://www.centuryply.com/centurylaminates/')
soup = BeautifulSoup(source.content, 'lxml')


for main in soup.select('li.dropdown-submenu'):
    for a_link in main.find_all('a'):
        try:
            t_link = a_link['href'].replace('#','')
            f_name = t_link.replace('.php','')
            m_link = f'https://www.centuryply.com/centurylaminates/{t_link}'

            folder_location = f'./data/{f_name}'
            if not os.path.exists(folder_location):
                os.mkdir(folder_location)




            source = requests.get(m_link)
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
                name = f' {name} '
                print(name)

                desc = soup.find('div',class_='product-description').p.text
                print(desc)
                
                f_name = name.replace(' ','_')
                filenames = f'{folder_location}/{f_name}.csv'
                with open(filenames , 'w') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['Prod_link ',' Name ',' Images ', ' Prod_Desc '])
                    csv_writer.writerow([link , name , prod_img , desc])
                print(csv_file.closed)

            

        except:
            print('')







    