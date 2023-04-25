from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Prod_link','Images','name', 'Prod_tags','Prod_desc','Prod_warranty','Prod_size','Prod_usps','Prod_spec','Prod_specinpoint','Prod_Tech_Specification'])

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

    sections = ['https://www.centuryply.com/centurydoors/century-club-prime-doors', 'https://www.centuryply.com/centurydoors/bond-doors', 'https://www.centuryply.com/centurydoors/sainik-doors',
                'https://www.centuryply.com/centurydoors/century-melamine-doors-skin', 'https://www.centuryply.com/centurydoors/century-metallic-doors-skin', 'https://www.centuryply.com/centurydoors/century-plain-doors-skin', 'https://www.centuryply.com/centurydoors/century-white-primered-door-skin',
                'https://www.centuryply.com/centurydoors/century-laminated-doors', 'https://www.centuryply.com/centurydoors/century-veneer-doors', 'https://www.centuryply.com/centurydoors/sainik-laminated-doors']
    file_names = [
        './Century Doors/Flush Doors/club-prime-doors.csv',
        './Century Doors/Flush Doors/bond-doors.csv',
        './Century Doors/Flush Doors/sainik-doors.csv',
        './Century Doors/Panel Moulded Doors/century-melamine-doors.csv',
        './Century Doors/Panel Moulded Doors/century-metallic-doors-skin.csv',
        './Century Doors/Panel Moulded Doors/century-plain-doors-skin.csv',
        './Century Doors/Panel Moulded Doors/century-white-premiered-doors-skin.csv',
        './Century Doors/Decorative Doors/century-laminated-doors.csv',
        './Century Doors/Decorative Doors/century-veneer-doors.csv',
        './Century Doors/Decorative Doors/sainik-laminated-doors.csv',
        
    ]


    scrape(sections, file_names)