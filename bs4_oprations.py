from functions.mysoup import soup

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

# advance
# find id and class
'''print(soup.find(id='b3')) 
print()
print(soup.find(class_="imran2"))
print(soup.find(class_="imran2").string)

'''

# find children
''' for child in soup.find(class_="container").children:
       print(child)
'''
# find parents
'''for p in soup.find(class_="container").parents:
    print(p)
'''


'''
 container = soup.find(class_="container") # find by class name using "class_"
container.name='span' # change tag div to span tag
container['class']=['mycontainer1','mycontainer2'] # add class names 
print(container)
'''
'''
ul_tag = soup.new_tag('ul')

li_tag = soup.new_tag('li')
li_tag.string = 'imran'
ul_tag.append(li_tag)

li_tag = soup.new_tag('li')
li_tag.string = 'irfan'
ul_tag.append(li_tag)

li_tag = soup.new_tag('li')
li_tag.string = 'muskan'
ul_tag.append(li_tag)

soup.body.insert_before(ul_tag)

with open("data/modified.html", "w") as f:
    f.write(str(soup))
'''

# write_functions
from functions import bs4_functions  as bs4fun

'''
# get all classes,ids,content and so on using above packages
results = soup.find(bs4fun.has_class)
for result in results:
    print(result)'''
    # print(result.string)

get_id = bs4fun.has_id_para("b1")
get_class = bs4fun.has_class_para("imran")
get_classes = soup.find_all(bs4fun.has_class)
get_ids = soup.find_all(bs4fun.has_id)
print('----------id------------')
print('id ',get_id)
print('----------ids------------')
print('ids ',get_ids)
print('----------class------------')
print('class ',get_class)
print('---------classes-------------')
print('classes ',get_classes)



