
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
​
#from selenium.webdriver.support import expected_conditions
​
site="https://www.etsy.com/in-en/listing/171816901/12-carat-gold-diamond-earrings-14k-white?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sr_gallery-1-8&frs=1"
browser = webdriver.Chrome(executable_path="D:\chromedriver")
browser.get(site)
user_agent = {'User-agent': 'Chrome'}
source = requests.get(site ,headers = user_agent).text
soup = BeautifulSoup(source, "lxml")
​
 A=[]
​
for j in range (1,15):
    
    for i in range(0,4):
        review_part=browser.find_element_by_xpath('//*[@id="review-preview-toggle-'+str(i)+'"]')        
        A.append(review_part.text.strip())
        
    #myreviewxpath//*[@id="review-preview-toggle-0"]
    next_1 = browser.find_element_by_xpath('//*[@id="reviews"]/div[2]/nav/ul/li[position() = last()]/a')
    next_1.click()                         
    sleep(5)
    #mynextxpath..//*[@id="reviews"]/div[2]/nav/ul/li[3]/a/span[2]
    #mypathnext'//*[@id="reviews"]/div[2]/nav/ul/li[2]/a/span['+str(j)+']'
​
import pandas as pd
​dff = pd.DataFrame()
​dff['Reviews_df'] = A
​dff.to_csv('ETSY.csv', index = False)
​
#database
​
import sqlite3 as sql
import pandas as pd
​
#open the connection
conn = sql.connect('ETSY.db')
​
dff.to_sql('Rev', conn , index=False)
cursor = conn.cursor()
cursor.execute("SELECT * FROM Rev")
for record in cursor:
    print(record)
​

​
​
#conn.execute('SELECT * FROM Review').fetchall()
​
​
#conn.execute('SELECT * FROM Review').fetchone()
​
​
'''
#one more way using the object of sql
​
conn = sql.connect('ETSY.db')
cursor = conn.cursor()
​
cursor.execute("SELECT * FROM Review")
​
for record in cursor:
    print (record)
'''


