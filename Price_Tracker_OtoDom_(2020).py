import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re

URL = 'https://www.otodom.pl/sprzedaz/mieszkanie/krakow/?search%5Bregion_id%5D=6&search%5Bsubregion_id%5D=410&search%5Bcity_id%5D=38&search%5Bdistrict_id%5D=62'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}



def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    soup2 = BeautifulSoup(soup.prettify(), 'lxml')

    try:
        title = soup2.find(class_="offer-item-title")
        price = soup2.find(class_="offer-item-price")

    except:
        print("Some error occured :(")

    pat1 = re.compile(r'([1-9][0-9]{,2}\s[0-9]{,3})\s', flags=re.DOTALL)
    pat2 = re.compile(r'\"\>\s*(.*?)\s*\<\/', flags=re.DOTALL)

    matches = pat1.search(str(price))
    matches2 = pat2.search(str(title))
    fin_price = matches.group(1)
    fin_price = fin_price.replace(" ", "")
    print(int(fin_price))
    fin_title = matches2.group(1)

    if fin_price == 439000:
        send_mail()
    return

def send_mail(fin_title, fin_price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('grayling96@gmail.com', 'squdkjmryygwoxys')

    subject = 'Wiadomość wysłana przez bota do sprawdzania pozycji ogłoszenia'
    body = 'Stworzyłem właśnie aplikacje która automatycznie wysyła maila gdy ogłoszenie osiągnie pierwszą pozycję. \n Treść ogłoszenia: {}, \t Cena: {} zł'.format(fin_title, fin_price)

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
    time.sleep(60)