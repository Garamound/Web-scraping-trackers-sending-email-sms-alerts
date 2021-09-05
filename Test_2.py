import re
from datetime import datetime
import matplotlib.pyplot as plt
import http.client

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
#    text=file.read().replace('\n', '')
#print(text)

str_current_state = re.findall(r"\"currentState\"\:\{(.+?)\}", text)
current_state_value = float((re.findall(r"\"value\"\:(\d*\.\d*)", str_current_state[0]))[0])
current_state_time = re.findall(r"\"date\"\:\"(.+?)\"", str_current_state[0])
#print(str_current_state)
#print(current_state_time)

str_state_values = re.findall(r"\"state\"\:\"(.+?).+?\"date\"\:\"(.+?)\:00Z\"\,\"value\"\:(.+?)\}", text)

state_values_time_list = []
state_values_level_list = []

for item in reversed(str_state_values):
    state_values_time_list.append(item[1].replace('T', ' '))
    state_values_level_list.append(float(item[2]))

#print(state_values_time_list)
#print(state_values_level_list)

now = datetime.now()
plot = plt.plot(state_values_time_list, state_values_level_list, 'ro')
plt.title("Stan wody w Bielanach: " + str(now))
plt.xlabel('Time')
plt.ylabel('Water Level (cm)')
ax = plt.gca()
plt.xticks(rotation=90)
for label in ax.get_xaxis().get_ticklabels()[::2]:
    label.set_visible(False)
plt.grid(True)
plt.show()

# datetime object containing current date and time
#print(now)

