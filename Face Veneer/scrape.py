from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Prod_link','Images','name', 'Prod_tags','Prod_desc','Prod_size','Prod_usps','Prod_specification','Prod_specinpoint'])

            print(f'> {sections[i]}')
            
            
            url = f'{sections[i]}'
            source = requests.get(url)
            soup = BeautifulSoup(source.content, 'lxml')

            l=[]
            t = []
            s = []
            main = soup.find('div',class_='product-description')
            img1 = main.find('div',class_='tabcontent',id ='thumb1').span.img['src']
            p_img1 = f'https://www.centuryply.com/{img1}'
            prod_img = f'{p_img1}'
            prod_img = prod_img.replace('\r\n','')
            print(prod_img)

            prod_name = main.find('div',class_='content').h1.text.strip()
            print(prod_name)

            prod_tags = main.find('div',class_='bytags').text.replace('\n','')
            print(prod_tags)

            prod_desc = main.find('div',class_='pr-content').br.previous_sibling.strip()
            prod_desc = prod_desc.replace('\r\n','')
            print(prod_desc)

            prod_size = soup.find('ul',class_='description_list inlinred').text.strip()
            print(prod_size)


            prod_info = soup.find('section',class_='block-usp nofaqpad')

            for p_usp in prod_info.find_all('li'):
                prod_usp = p_usp.div.strong.text
                l.append(prod_usp)

            prod_usps = ' , '.join(str(e) for e in l)
            prod_usps = prod_usps.replace('\r\n','')
            print(prod_usps)

            p_spec = soup.find('div',class_='faq-answer')
            prod_spec = p_spec.p.text
            print(prod_spec)

            for p_specification in p_spec.find_all('li'):
                prod_specification = p_specification.h5.text
                t.append(prod_specification)

            prod_spec_point = ' , '.join(str(e) for e in t)
            prod_spec_point = prod_spec_point.replace('\r\n','')
            print(prod_spec_point)
                
            csv_writer.writerow([sections[i],prod_img,prod_name,prod_tags,prod_desc,prod_size,prod_usps,prod_spec,prod_spec_point])



            

if __name__ == '__main__':

    '''
    usage:
    -> install requirements
    -> verify:
        - all site sections are listed in `sections`
        - all sites have a corresponding csv file `file_names`
        - all paths to the csv file are correct
    -> run
    '''

    sections = ['https://www.centuryply.com/face-veneer/face-veneer']

    file_names = [
        './Face Veneer/Face-Veneer.csv',
         ]


    scrape(sections, file_names)