from dotenv import dotenv_values
from functions.time_decorator import time_calculation
from bs4 import BeautifulSoup
import requests 
from functions import bs4_functions as bs4fun
import convertion as con
import multiprocessing 
import time
env_vars = dotenv_values('.env')


@time_calculation
def flipkart_scrap():
    title_lst,price_lst=[],[]
    url = env_vars.get('flipkart_path')
    r = requests.get(str(url))
    soup = BeautifulSoup(r.content,'html.parser')
    titles_  = bs4fun.has_classall_para(soup,"_4rR01T")
    price_  = bs4fun.has_classall_para(soup,"_30jeq3 _1_WHN1")
    for t in titles_:
        title_lst.append(t.get_text())
    for p in price_:
        pencode = p.get_text()
        pcode = pencode.replace('?', '₹')
        price_lst.append(pcode)
    con.df_to_csv(title_lst,price_lst)
    return title_lst,price_lst

if __name__=="__main__":
    flipkart_scrap()

