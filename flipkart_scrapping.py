from dotenv import dotenv_values
from functions.time_decorator import time_calculation
from bs4 import BeautifulSoup
import requests 
from functions import bs4_functions as bs4fun
import convertion as con

@time_calculation
def flipkart_scrap(env_vars,title_lst,price_lst):
    url = env_vars.get('flipkart_path')
    r = requests.get(str(url))
    soup = BeautifulSoup(r.content,'html.parser')
    titles_  = bs4fun.has_classall_para(soup,"_4rR01T")
    price_  = bs4fun.has_classall_para(soup,"_30jeq3 _1_WHN1")
    if titles_ and price_:
        title_lst = [t.get_text() for t in titles_]
        price_lst = [p.get_text().replace('?', '₹') for p in price_]
    else:
        print("No titles   prices found.")
        return None, None
    # con.df_to_csv(title_lst,price_lst)
    con.df_to_mysql(title_lst,price_lst)
    return title_lst,price_lst
if __name__=="__main__":
    env_vars = dotenv_values('.env')
    title_lst,price_lst=[],[]
    flipkart_scrap(env_vars,title_lst,price_lst)

