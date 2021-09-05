import requests
import http.client
from datetime import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
import smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage


conn = http.client.HTTPSConnection("hydro.imgw.pl")
payload = ""
headers = {
    'Connection': "keep-alive",
    'sec-ch-ua': "^\^Chromium^^;v=^\^92^^, ^\^"
    }
conn.request("GET", "/api/station/hydro?id=150190340", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
text = data.decode("utf-8")
#with open("txt.txt", encoding="utf8") as file:
    #text=file.read().replace('\n', '')
print(text)

str_current_state = re.findall(r"\"currentState\"\:\{(.+?)\}", text)
current_state_value = float((re.findall(r"\"value\"\:(\d*\.\d*)", str_current_state[0]))[0])
current_state_time = re.findall(r"\"date\"\:\"(.+?)\"", str_current_state[0])
#print(str_current_state)
#print(current_state_time)

str_state_values = re.findall(r"\"state\"\:\"(.+?).+?\"date\"\:\"(.+?)\:00Z\"\,\"value\"\:(.+?)\}", text)
flow_values = re.findall(r"value\"\:(.{,6})\,\"dreId\"\:1099", text)

state_values_time_list = []
state_values_level_list = []
flow_values_list = []

for item in reversed(str_state_values):
    state_values_time_list.append(item[1].replace('T', ' '))
    state_values_level_list.append(float(item[2]))

for item in flow_values: flow_values_list.append(float(item)), print(item)
flow_values.reverse()
flow_values_list.append(flow_values_list[-1])
#flow_values_list = reversed(flow_values_list)

#print(len(flow_values_list), len(state_values_level_list), len(state_values_time_list))
print(flow_values_list)


# Creatina a darker areas of the plot to indicate day and night. Converting hours to numbers.

integer_hours_list = []
night_hours_list = []
for date in state_values_time_list:
    date = date[-5: -1].replace(":", "")
    if date[0] == '0': date = date[1:3]
    integer_hours_list.append(int(date))

URL = 'https://meteogram.pl/'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = str(BeautifulSoup(page.content, 'html.parser'))[8700: 9300]
sunrise = int(re.findall(r".+?rise\"\>0?(.+?)\ \<", soup)[0].replace(":", "")[:-1])
sunset = int(re.findall(r".+?set\"\>0?(.+?)\ \<", soup)[0].replace(":", "")[:-1])

for index, item in enumerate(integer_hours_list):
    if item > sunset or item < sunrise: night_hours_list.append(index)

# Plotting with matplotlib

now = datetime.now()
plt.figure(figsize=(12, 7))
plot = plt.plot(state_values_time_list, state_values_level_list, '-ro', markersize=4, zorder=1)



plt.title("Stan wody w Bielanach  " + str(now))
plt.xlabel('Time')
plt.ylabel('Water Level (cm)')
ax = plt.gca()

plt.xticks(rotation=90)
for label in ax.get_xaxis().get_ticklabels()[::2]:
    label.set_visible(False)

for i in night_hours_list:   # Darker areas for day and night
    plt.axvspan(i, i+1, facecolor='0.2', alpha=0.15)

axis2 = plt.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
axis2.set_ylabel('Flow', color=color)  # we already handled the x-label with ax1
axis2.plot(state_values_time_list, flow_values_list, color=color)
axis2.tick_params(axis='y', labelcolor=color)



plt.grid(True)
plt.show()
plt.savefig('Stan_wody-Bielany.png')

img_format = 'png'
image_paths = ['C:/Users/Admin/PycharmProjects/Price_Tracker/Stan_wody-Bielany.png']

# Sending Email

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    #with open('Stan_wody-Bielany.png', 'rb') as f:

    text_part = msg.iter_parts()
    text_part
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <p>Hi Paul,</p>
            <p>If you are seeing this, it means that you have received my email. Check out these images!</p>
            <p>Best,</p>
            <p>Paul</p>
            <img src="cid:Stan_wody-Bielany" ><br>
        </body>
    </html>
    """, subtype='html')

    counter = 1
    for fp in image_paths:
        fp = open(fp, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image' + str(counter) + '>')
        msg.attach(msgImage)
        counter += 1

    user = "pikeystrikes@gmail.com"
    msg['from'] = user
    password = 'agveazinghufpfce'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

#if __name__ == "__main__":
    #email_alert("Hey", "Hello", "grayling96@gmail.com")