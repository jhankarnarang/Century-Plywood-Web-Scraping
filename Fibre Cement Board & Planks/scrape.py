from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Prod_link','Images','name', 'Prod_tags','Prod_desc','Prod_warranty','Prod_size','Prod_usps'])

            print(f'> {sections[i]}')
            
            
            url = f'{sections[i]}'
            source = requests.get(url)
            soup = BeautifulSoup(source.content, 'lxml')

            l=[]
            t = []
            s = []
            main = soup.find('div',class_='product-description')
            img1 = main.find('div',class_='tabcontent',id ='thumb1').span.img['src']
            img2 = main.find('div',class_='tabcontent',id ='thumb2').span.img['src']
            p_img1 = f'https://www.centuryply.com/{img1}'
            p_img2 = f'https://www.centuryply.com/{img2}'
            prod_img = f'{p_img1} , {p_img2}'
            prod_img = prod_img.replace('\r\n','')
            print(prod_img)

            prod_name = main.find('div',class_='content').h1.text.strip()
            print(prod_name)

            prod_tags = main.find('div',class_='bytags').text.replace('\n','')
            print(prod_tags)

            prod_desc = main.find('div',class_='pr-content').br.previous_sibling.strip()
            print(prod_desc)

            prod_warranty = main.find('div',class_='pr-content').b.text
            print(prod_warranty)

            prod_size = soup.find('ul',class_='description_list inlinred').text.strip()
            print(prod_size)


            prod_info = soup.find('section',class_='block-usp nofaqpad')

            for p_usp in prod_info.find_all('li'):
                prod_usp = p_usp.div.strong.text
                l.append(prod_usp)

            prod_usps = ' , '.join(str(e) for e in l)
            prod_usps = prod_usps.replace('\r\n','')
            print(prod_usps)
                
            csv_writer.writerow([sections[i],prod_img,prod_name,prod_tags,prod_desc,prod_warranty,prod_size,prod_usps])



            

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

    sections = ['https://www.centuryply.com/zykron-fibre-cement-board/zykron-HD-Board', 'https://www.centuryply.com/zykron-fibre-cement-board/zykron-siding-board']

    file_names = [
        './Fibre Cement Board & Planks/zykron-HD-Board.csv',
        './Fibre Cement Board & Planks/zykron-siding-Board.csv',
         ]


    scrape(sections, file_names)