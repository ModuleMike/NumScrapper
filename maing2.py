import re module


# initializing string
test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'

# initializing tag
tag = "b"

# finding the index of the first occurrence of the opening tag
start_idx = test_str.find("<" + tag + ">")

# initializing an empty list to store the extracted strings
res = []

# extracting the strings between the tags
while start_idx != -1:
	end_idx = test_str.find("</" + tag + ">", start_idx)
	if end_idx == -1:
		break
	res.append(test_str[start_idx+len(tag)+2:end_idx])
	start_idx = test_str.find("<" + tag + ">", end_idx)

# printing the extracted strings
print("The Strings extracted : " + str(res))





x = soup.ul.children

for child in soup.ul.children:
    print(child)

x = soup.find_all('td', attrs={'class': 'game-balls'})



chunks = [(win_num[i:i+chunk_size]) for i in range(0, len(win_num), chunk_size)]
print(chunks)

x = win_num.split(',')

for i in range(start, end, 2):
    print(x[i:i+2])

print(len(x))