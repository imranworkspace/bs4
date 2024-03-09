from bs4 import BeautifulSoup
try:
    with open('data/sample.html','r') as f:
        html_file = f.read()
except FileNotFoundError as e:
    print(f'{e.filename} file does not exist')
else:
    soup = BeautifulSoup(html_file,'html.parser')