###  before running you must put your Gmail credentials in the first line of block #3 !!!

from bs4 import BeautifulSoup                                    
import requests                                  

from urllib.parse import urlparse, parse_qsl               #-- for py3.9 and earlier use parse_qs
import yagmail  

m = input("How many messages? ")

n = int(m)

i = n

while i > 0: 

    # 1- scrape Pravdamail frontpage to extract messaging URL

    page = requests.get('https://pravdamail.com').text

    soup = BeautifulSoup(page, 'html.parser')      

    links = soup.find_all('a') 

    gmail = links[9] 

    URL = gmail.get('href')  

    # 2 - Parse the URL into email params

    parsed_url = urlparse(URL)     

    query_dict = dict(parse_qsl(parsed_url.query))                  

    #for py3.9 and earlier use -- query_dict = parse_qs(parsed_url.query) -- in place of line above

    subject = query_dict['subject']     

    receiver_email = query_dict['to']

    text = query_dict['body']


    # 3 - setup email 

    yag = yagmail.SMTP('<GMAIL ACCOUNT NAME>', '<APP-SPECIFIC GMAIL PASSWORD>') #Gmail credentials go here!
    contents = text
    yag.send(receiver_email, subject, contents)
  
    
    i = i - 1

   
    print ('Message ' + str(n-i) + ' of ' + m + " sent.")


print('pyRavda succeeded in sending ' + m + ' messages to Russia.')
