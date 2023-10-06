import requests
from bs4 import BeautifulSoup
from collections import Counter

# ------------------------ Start of 2023 ------------------------

# URL to web-site
url_2023 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2023"

# Sends requests to URL
request_2023 = requests.get(url_2023)

# Takes request converts to text
html_2023 = request_2023.text

# HTML parser with use of BeautifulSoup
soup_2023 = BeautifulSoup(html_2023, 'html.parser')

# Assigns variable data with parsed soup for all elements that are 'td' and class = 'game-balls'
data_2023 = soup_2023.find_all('td', class_="game-balls")

# Creates dictionary container to house each set of winning numbers and remove duplicates generated in web-site html
data_nums_dict_2023 = {}
key = 0
for win_nums in data_2023[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2023[key] = val
# print(data_nums_dict_2023)

pow_nums_dict_2023 = {}
key = 0
for win_nums in data_2023[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2023[key] = val
# print(pow_nums_dict_2023)

# Creates list container to house the combination of all winning numbers
data_nums_list_2023 = []
for key in data_nums_dict_2023:
    data_nums_list_2023 = data_nums_list_2023 + data_nums_dict_2023[key]
    key += 1
# print(data_num_list_2023)

# Counts number of winning numbers
data_count_list_2023 = Counter(data_nums_list_2023)
print(f"2023 -- Power Ball Number {data_count_list_2023} \n")

# Creates list container to house the combination of all power ball winning numbers
pow_nums_list_2023 = []
for key in pow_nums_dict_2023:
    pow_nums_list_2023 = pow_nums_list_2023 + pow_nums_dict_2023[key]
    key += 1

# Counts number of power ball winning numbers
pow_count_list_2023 = Counter(pow_nums_list_2023)
print(f"2023 -- Power Ball Number {pow_count_list_2023} \n")

# ------------------------- End of 2023 -------------------------


# ------------------------ Start of 2022 ------------------------

url_2022 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2022"

request_2022 = requests.get(url_2022)

html_2022 = request_2022.text

soup_2022 = BeautifulSoup(html_2022, 'html.parser')

data_2022 = soup_2022.find_all('td', class_="game-balls")

data_nums_dict_2022 = {}
key = 0
for win_nums in data_2022[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2022[key] = val

pow_nums_dict_2022 = {}
key = 0
for win_nums in data_2022[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2022[key] = val

data_nums_list_2022 = []
for key in data_nums_dict_2022:
    data_nums_list_2022 = data_nums_list_2022 + data_nums_dict_2022[key]
    key += 1

data_count_list_2022 = Counter(data_nums_list_2022)
print(f"2022 -- Power Ball Number {data_count_list_2022} \n")

pow_nums_list_2022 = []
for key in pow_nums_dict_2022:
    pow_nums_list_2022 = pow_nums_list_2022 + pow_nums_dict_2022[key]
    key += 1

pow_count_list_2022 = Counter(pow_nums_list_2022)
print(f"2022 -- Power Ball Number {pow_count_list_2022} \n")


# ------------------------- End of 2022 -------------------------

# ------------------------ Start of 2021 ------------------------

url_2021 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2021"

request_2021 = requests.get(url_2021)

html_2021 = request_2021.text

soup_2021 = BeautifulSoup(html_2021, 'html.parser')

data_2021 = soup_2021.find_all('td', class_="game-balls")

data_nums_dict_2021 = {}
key = 0
for win_nums in data_2021[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2021[key] = val

pow_nums_dict_2021 = {}
key = 0
for win_nums in data_2021[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2021[key] = val

data_nums_list_2021 = []
for key in data_nums_dict_2021:
    data_nums_list_2021 = data_nums_list_2021 + data_nums_dict_2021[key]
    key += 1

data_count_list_2021 = Counter(data_nums_list_2021)
print(f"2021 -- Power Ball Number {data_count_list_2021} \n")

pow_nums_list_2021 = []
for key in pow_nums_dict_2021:
    pow_nums_list_2021 = pow_nums_list_2021 + pow_nums_dict_2021[key]
    key += 1

pow_count_list_2021 = Counter(pow_nums_list_2021)
print(f"2021 -- Power Ball Number {pow_count_list_2021} \n")

# ------------------------- End of 2021 -------------------------

# ------------------------ Start of 2020 ------------------------

url_2020 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2020"

request_2020 = requests.get(url_2020)

html_2020 = request_2020.text

soup_2020 = BeautifulSoup(html_2020, 'html.parser')

data_2020 = soup_2020.find_all('td', class_="game-balls")

data_nums_dict_2020 = {}
key = 0
for win_nums in data_2020[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2020[key] = val

pow_nums_dict_2020 = {}
key = 0
for win_nums in data_2020[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2020[key] = val

data_nums_list_2020 = []
for key in data_nums_dict_2020:
    data_nums_list_2020 = data_nums_list_2020 + data_nums_dict_2020[key]
    key += 1

data_count_list_2020 = Counter(data_nums_list_2020)
print(f"2020 -- Power Ball Number {data_count_list_2020} \n")

pow_nums_list_2020 = []
for key in pow_nums_dict_2020:
    pow_nums_list_2020 = pow_nums_list_2020 + pow_nums_dict_2020[key]
    key += 1

pow_count_list_2020 = Counter(pow_nums_list_2020)
print(f"2020 -- Power Ball Number {pow_count_list_2020} \n")

# ------------------------- End of 2020 -------------------------
# ------------------------ Start of 2019 ------------------------

url_2019 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2019"

request_2019 = requests.get(url_2019)

html_2019 = request_2019.text

soup_2019 = BeautifulSoup(html_2019, 'html.parser')

data_2019 = soup_2019.find_all('td', class_="game-balls")

data_nums_dict_2019 = {}
key = 0
for win_nums in data_2019[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2019[key] = val

pow_nums_dict_2019 = {}
key = 0
for win_nums in data_2019[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2019[key] = val

data_nums_list_2019 = []
for key in data_nums_dict_2019:
    data_nums_list_2019 = data_nums_list_2019 + data_nums_dict_2019[key]
    key += 1

data_count_list_2019 = Counter(data_nums_list_2019)
print(f"2019 -- Power Ball Number {data_count_list_2019} \n")

pow_nums_list_2019 = []
for key in pow_nums_dict_2019:
    pow_nums_list_2019 = pow_nums_list_2019 + pow_nums_dict_2019[key]
    key += 1

pow_count_list_2019 = Counter(pow_nums_list_2019)
print(f"2019 -- Power Ball Number {pow_count_list_2019} \n")

# ------------------------- End of 2019 -------------------------

# ------------------------ Start of 2018 ------------------------

url_2018 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2018"

request_2018 = requests.get(url_2018)

html_2018 = request_2018.text

soup_2018 = BeautifulSoup(html_2018, 'html.parser')

data_2018 = soup_2018.find_all('td', class_="game-balls")

data_nums_dict_2018 = {}
key = 0
for win_nums in data_2018[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2018[key] = val

pow_nums_dict_2018 = {}
key = 0
for win_nums in data_2018[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2018[key] = val

data_nums_list_2018 = []
for key in data_nums_dict_2018:
    data_nums_list_2018 = data_nums_list_2018 + data_nums_dict_2018[key]
    key += 1

data_count_list_2018 = Counter(data_nums_list_2018)
print(f"2018 -- Power Ball Number {data_count_list_2018} \n")

pow_nums_list_2018 = []
for key in pow_nums_dict_2018:
    pow_nums_list_2018 = pow_nums_list_2018 + pow_nums_dict_2018[key]
    key += 1

pow_count_list_2018 = Counter(pow_nums_list_2018)
print(f"2018 -- Power Ball Number {pow_count_list_2018} \n")

# ------------------------- End of 2018 -------------------------

# ------------------------ Start of 2017 ------------------------

url_2017 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2017"

request_2017 = requests.get(url_2017)

html_2017 = request_2017.text

soup_2017 = BeautifulSoup(html_2017, 'html.parser')

data_2017 = soup_2017.find_all('td', class_="game-balls")

data_nums_dict_2017 = {}
key = 0
for win_nums in data_2017[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2017[key] = val

pow_nums_dict_2017 = {}
key = 0
for win_nums in data_2017[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2017[key] = val

data_nums_list_2017 = []
for key in data_nums_dict_2017:
    data_nums_list_2017 = data_nums_list_2017 + data_nums_dict_2017[key]
    key += 1

data_count_list_2017 = Counter(data_nums_list_2017)
print(f"2017 -- Power Ball Number {data_count_list_2017} \n")

pow_nums_list_2017 = []
for key in pow_nums_dict_2017:
    pow_nums_list_2017 = pow_nums_list_2017 + pow_nums_dict_2017[key]
    key += 1

pow_count_list_2017 = Counter(pow_nums_list_2017)
print(f"2017 -- Power Ball Number {pow_count_list_2017} \n")

# ------------------------- End of 2017 -------------------------

# ------------------------ Start of 2016 ------------------------

url_2016 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2016"

request_2016 = requests.get(url_2016)

html_2016 = request_2016.text

soup_2016 = BeautifulSoup(html_2016, 'html.parser')

data_2016 = soup_2016.find_all('td', class_="game-balls")

data_nums_dict_2016 = {}
key = 0
for win_nums in data_2016[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2016[key] = val

pow_nums_dict_2016 = {}
key = 0
for win_nums in data_2016[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2016[key] = val

data_nums_list_2016 = []
for key in data_nums_dict_2016:
    data_nums_list_2016 = data_nums_list_2016 + data_nums_dict_2016[key]
    key += 1

data_count_list_2016 = Counter(data_nums_list_2016)
print(f"2016 -- Power Ball Number {data_count_list_2016} \n")

pow_nums_list_2016 = []
for key in pow_nums_dict_2016:
    pow_nums_list_2016 = pow_nums_list_2016 + pow_nums_dict_2016[key]
    key += 1

pow_count_list_2016 = Counter(pow_nums_list_2016)
print(f"2016 -- Power Ball Number {pow_count_list_2016} \n")

# ------------------------- End of 2016 -------------------------

# ------------------------ Start of 2015 ------------------------

url_2015 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2015"

request_2015 = requests.get(url_2015)

html_2015 = request_2015.text

soup_2015 = BeautifulSoup(html_2015, 'html.parser')

data_2015 = soup_2015.find_all('td', class_="game-balls")

data_nums_dict_2015 = {}
key = 0
for win_nums in data_2015[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2015[key] = val

pow_nums_dict_2015 = {}
key = 0
for win_nums in data_2015[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2015[key] = val

data_nums_list_2015 = []
for key in data_nums_dict_2015:
    data_nums_list_2015 = data_nums_list_2015 + data_nums_dict_2015[key]
    key += 1

data_count_list_2015 = Counter(data_nums_list_2015)
print(f"2015 -- Power Ball Number {data_count_list_2015} \n")

pow_nums_list_2015 = []
for key in pow_nums_dict_2015:
    pow_nums_list_2015 = pow_nums_list_2015 + pow_nums_dict_2015[key]
    key += 1

pow_count_list_2015 = Counter(pow_nums_list_2015)
print(f"2015 -- Power Ball Number {pow_count_list_2015} \n")

# ------------------------- End of 2015 -------------------------

# ------------------------ Start of 2014 ------------------------

url_2014 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2014"

request_2014 = requests.get(url_2014)

html_2014 = request_2014.text

soup_2014 = BeautifulSoup(html_2014, 'html.parser')

data_2014 = soup_2014.find_all('td', class_="game-balls")

data_nums_dict_2014 = {}
key = 0
for win_nums in data_2014[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2014[key] = val

pow_nums_dict_2014 = {}
key = 0
for win_nums in data_2014[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2014[key] = val

data_nums_list_2014 = []
for key in data_nums_dict_2014:
    data_nums_list_2014 = data_nums_list_2014 + data_nums_dict_2014[key]
    key += 1

data_count_list_2014 = Counter(data_nums_list_2014)
print(f"2014 -- Power Ball Number {data_count_list_2014} \n")

pow_nums_list_2014 = []
for key in pow_nums_dict_2014:
    pow_nums_list_2014 = pow_nums_list_2014 + pow_nums_dict_2014[key]
    key += 1

pow_count_list_2014 = Counter(pow_nums_list_2014)
print(f"2014 -- Power Ball Number {pow_count_list_2014} \n")

# ------------------------- End of 2014 -------------------------

# ------------------------ Start of 2013 ------------------------

url_2013 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2013"

request_2013 = requests.get(url_2013)

html_2013 = request_2013.text

soup_2013 = BeautifulSoup(html_2013, 'html.parser')

data_2013 = soup_2013.find_all('td', class_="game-balls")

data_nums_dict_2013 = {}
key = 0
for win_nums in data_2013[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2013[key] = val

pow_nums_dict_2013 = {}
key = 0
for win_nums in data_2013[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2013[key] = val

data_nums_list_2013 = []
for key in data_nums_dict_2013:
    data_nums_list_2013 = data_nums_list_2013 + data_nums_dict_2013[key]
    key += 1

data_count_list_2013 = Counter(data_nums_list_2013)
print(f"2013 -- Power Ball Number {data_count_list_2013} \n")

pow_nums_list_2013 = []
for key in pow_nums_dict_2013:
    pow_nums_list_2013 = pow_nums_list_2013 + pow_nums_dict_2013[key]
    key += 1

pow_count_list_2013 = Counter(pow_nums_list_2013)
print(f"2013 -- Power Ball Number {pow_count_list_2013} \n")

# ------------------------- End of 2013 -------------------------

# ------------------------ Start of 2012 ------------------------

url_2012 = "https://www.walottery.com/WinningNumbers/PastDrawings.aspx?gamename=megamillions&unittype=year&unitcount=2013"

request_2012 = requests.get(url_2012)

html_2012 = request_2013.text

soup_2012 = BeautifulSoup(html_2012, 'html.parser')

data_2012 = soup_2012.find_all('td', class_="game-balls")

data_nums_dict_2012 = {}
key = 0
for win_nums in data_2012[::2]:
    key += 1
    val = win_nums.text.split()[0:5]
    data_nums_dict_2012[key] = val

pow_nums_dict_2012 = {}
key = 0
for win_nums in data_2012[::2]:
    key += 1
    val = win_nums.text.split()[5:6]
    pow_nums_dict_2012[key] = val

data_nums_list_2012 = []
for key in data_nums_dict_2012:
    data_nums_list_2012 = data_nums_list_2012 + data_nums_dict_2012[key]
    key += 1

data_count_list_2012 = Counter(data_nums_list_2012)
print(f"2012 -- Power Ball Number {data_count_list_2012} \n")

pow_nums_list_2012 = []
for key in pow_nums_dict_2012:
    pow_nums_list_2012 = pow_nums_list_2012 + pow_nums_dict_2012[key]
    key += 1

pow_count_list_2012 = Counter(pow_nums_list_2012)
print(f"2012 -- Power Ball Number {pow_count_list_2012} \n")

# ------------------------- End of 2012 -------------------------
# Beginning with the October 31, 2017 drawing, the game matrix changed from &#34;1 to 75&#34; white balls to
# &#34;1 to 70&#34; white balls, and from &#34;1 to 15&#34; Mega Balls to &#34;1 to 25&#34; Mega Balls.

# Beginning with the October 22, 2013 drawing, the game matrix changed from &#39;1 to 56&#39; white balls to
# &#39;1 to 75&#39; white balls, and from &#39;1 to 46&#39; mega balls to &#39;1 to 15&#39; mega balls. A
# 5 megaplier was also added
# ------------------------ Running Total -------------------------

num_total_count = [data_count_list_2023 + data_count_list_2022 +
                   data_count_list_2021 + data_count_list_2020 +
                   data_count_list_2019 + data_count_list_2018 +
                   data_count_list_2017 + data_count_list_2016 +
                   data_count_list_2015 + data_count_list_2014 +
                   data_count_list_2013 + data_count_list_2012]
print(f"The Total Hits Per Regular Number {num_total_count} \n")

pow_total_count = [pow_count_list_2023 + pow_count_list_2022 +
                   pow_count_list_2021 + pow_count_list_2020 +
                   pow_count_list_2019 + pow_count_list_2018 +
                   pow_count_list_2017 + pow_count_list_2016 +
                   pow_count_list_2015 + pow_count_list_2014 +
                   pow_count_list_2013 + pow_count_list_2012]
print(f"The Total Hits Per Power Ball Number {pow_total_count} \n")

# --------------------------- The End ----------------------------
