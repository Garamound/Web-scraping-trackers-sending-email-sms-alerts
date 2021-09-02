import requests
from bs4 import BeautifulSoup
import smtplib
import time

#URL = 'https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1585945494&sr=8-2'
#URL = 'https://allegro.pl/oferta/aparat-sony-alpha-a7-ii-swietna-okazja-9044132131?bi_s=ads&bi_m=listing%3Adesktop%3Aquery&bi_c=NTU1ZmQzNDMtYTIzMC00OTZmLTk1MGItMzVlYzRlNzE0OGViAA&bi_t=ape&referrer=proxy&emission_unit_id=483e1766-8a64-4e73-91b0-7c5c19adcb67'
URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1585946797&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMjJWQjFHSUlKQ0JWJmVuY3J5cHRlZElkPUEwMjg2NjM5S08zVzlVUTBFNFQmZW5jcnlwdGVkQWRJZD1BMDk5MjkyNDNBODVGRVg5MDJINDQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
def check_price():
    try:
        title = soup.find(id="productTitle").get_text()
        price = soup.find(id="price_inside_buybox").get_text()
    except:
        print("Some error occured :(")

    price = price.replace(".", "")
    price = price.replace(",", ".")
    price = float(price.replace("€", ""))

    if (price < 1800):
        send_mail()

    print(price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('grayling96@gmail.com', 'squdkjmryygwoxys')

    subject = 'Price fell down'
    body = 'Check the link! \n https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1585946797&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMjJWQjFHSUlKQ0JWJmVuY3J5cHRlZElkPUEwMjg2NjM5S08zVzlVUTBFNFQmZW5jcnlwdGVkQWRJZD1BMDk5MjkyNDNBODVGRVg5MDJINDQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'grayling96@gmail.com',
        'grayling96@gmail.com',
        msg
    )
    print('Hey! Email has been sent!')

    server.quit()

while True:
    check_price()
    time.sleep(60 * 60)