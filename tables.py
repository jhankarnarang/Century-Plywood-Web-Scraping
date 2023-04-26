import pandas as pd
import csv 


from urllib.request import Request, urlopen

req = Request('https://www.centuryply.com/centurydoors/sainik-doors', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req,timeout=10).read()


# csv_file = open('Anchor_fire_retardant_marine_tables.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Properties','Technical Data'])

# Webpage url                                                                                                               
#url = ('https://www.kamdhenulimited.com/kamdhenu-pas-chemical-properties.php')

# Extract tables
dfs = pd.read_html(webpage)


# Get first table                                                                                                           
df = dfs[0]
#df1 = dfs[1]
pd.set_option('max_colwidth', 400)
print(df)


df.to_csv('technical specification.csv')
# df1.to_csv('python.csv')
#csv_writer.writerow([df,df1])

# Extract columns                                                                                                           
# df2 = df[['Test Prescribed in IS: 2202 (Part-I), 1999','Minimum Value for Conformity','Observed Value']]
# print(df2)