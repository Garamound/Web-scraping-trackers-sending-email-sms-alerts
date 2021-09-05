import requests
from bs4 import BeautifulSoup
import smtplib
import time

#URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1585946797&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMjJWQjFHSUlKQ0JWJmVuY3J5cHRlZElkPUEwMjg2NjM5S08zVzlVUTBFNFQmZW5jcnlwdGVkQWRJZD1BMDk5MjkyNDNBODVGRVg5MDJINDQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
URL = 'https://hydro.imgw.pl/#station/hydro/150190340'
#URL = ''

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

def check_price():
    try:
        title = soup.find(id="tooltip").get_text()
        print(title)
        price = soup.find(id="price_inside_buybox").get_text()
    except:
        print("Some error occured :(")

    price = price.replace(".", "")
    price = price.replace(",", ".")
    price = float(price.replace("€", ""))

    #if (price < 1800):
        #send_mail()
    print(price)

#check_price()