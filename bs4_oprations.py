from bs4 import BeautifulSoup

with open('data/sample.html','r') as f:
    html_file = f.read()
soup = BeautifulSoup(html_file,'html.parser')
# print(soup.prettify())
# print(soup.find_all("div"))
# print(soup.title)
# print(soup.title.string)

# print(soup.find('div'))

'''divs = soup.find_all('div')
for div in divs:
    # print(div)
    print(div.string) '''

''' anchors = soup.find_all('a')
print(type(anchors)) '''

''' for a in soup.find_all('a'):
    print(a.string) '''

# print(soup.getText())

# attrs used to get id of class of specific tag in dictionary format
'''
tag = soup.find_all('span')
for t in tag:
    print(t.attrs)
    print(t.attrs.keys())
    print() 
'''

for l in soup.find_all('li'):
    print(l.get('id'))