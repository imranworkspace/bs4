from bs4 import BeautifulSoup
from dotenv import dotenv_values
env_vars = dotenv_values('.env')

try:
    with open(env_vars.get('sample_html_path'),'r') as f:
        html_file = f.read()
except FileNotFoundError as e:
    print(f'{e.filename} file does not exist')
else:
    soup = BeautifulSoup(html_file,'html.parser')