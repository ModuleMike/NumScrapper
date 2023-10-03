import requests
from bs4 import BeautifulSoup

# URL to web-site
url = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2023"

# Sends requests to URL
response = requests.get(url)

# Takes request converts to text
html = response.text

# HTML parser with use of BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Assigns variable data with parsed soup for all elements that are 'td' and class = 'game-balls'
data = soup.find_all('td', class_="game-balls")

# Creates dictionary container to house each set of winning numbers and remove duplicates generated in web-site html
data_nums_dict = {}
key = 0
for win_nums in data[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict[key] = val
#print(data_nums_dict)

# Creates list container to house the combination of all winning numbers
data_num_list = []
for key in data_nums_dict:
    data_num_list = data_num_list + data_nums_dict[key]
    key += 1
print(data_num_list)

# Creates container for key to count total number of winning numbers
win_num_count = []
for val in range(0,70):
    val += 1
    win_num_count.append(val)
win_num_tup = (win_num_count)
#print(win_num_tup)

# Creates dictionary to store matching key and
#win_num_total = {}

#for i in data_num_list:
    #key +



#for i in d:
    #print(d[i])




