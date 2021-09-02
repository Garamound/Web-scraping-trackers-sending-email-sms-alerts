import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re

URL = 'https://www.google.com/search?sxsrf=ALeKk014I_-NKCwpn3iruBxBhLEnA99T-A%3A1586040927505&ei=XxCJXvK5HsuymwWR5L64Ag&q=hotel+szczawnica&oq=hotel+szczawnica&gs_lcp=CgZwc3ktYWIQDFAAWABgvarSEWgAcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiy5dTw7s_oAhVL2aYKHRGyDycQ4dUDCAw'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}


#print(soup.prettify())

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        title = soup.find_all(class_="rc")#.get_text()        KONIECZNE BĘDZIE WYSZUKIWANIE ZA POMOCĄ SAMEGO REGEX - KOLEJNO KAŻDE POJAWIENIE SIĘ "HTTPS://"
        print()

        pat0 = re.compile(r'(C4eCVc c).{,80}(a href="https://)(.*?)\/?(" ping)', flags=re.DOTALL)
        pat1 = re.compile(r'(CAIQAA).{,80}(a href="https://)(.*?)\/?(" ping)', flags=re.DOTALL)
        pat2 = re.compile(r'(CAsQAA).{,80}(a href="https://)(.*?)\/?(" ping)', flags=re.DOTALL)
        pat3 = re.compile(r'(CAkQAA).{,80}(a href="https://)(.*?)\/?(" ping)', flags=re.DOTALL)
        pat4 = re.compile(r'(CAIQAA).{,80}(a href="https://)(.*?)\/?(" ping)', flags=re.DOTALL)

        match0 = pat0.search(str(title))
        match1 = pat1.search(str(title))
        match2 = pat2.search(str(title))
        match3 = pat3.search(str(title))
        match4 = pat4.search(str(title))

        pos0 = match1.group(3)
        pos1 = match1.group(3)
        pos2 = match2.group(3)
        pos3 = match3.group(3)
        pos4 = match3.group(3)

        print(pos0)
        print(pos1)
        print(pos2)
        print(pos3)
        print(pos4)


    except:
        print("Some error occured :(")

    #print(title)
    return

'''
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

    server.quit()   '''

while True:
    check_price()
    time.sleep(20)