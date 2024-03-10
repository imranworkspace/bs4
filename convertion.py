import pandas as pd
from functions.mysoup import env_vars
from sqlalchemy import create_engine

def df_to_csv(title_lst,price_lst):
    if len(title_lst) != len(price_lst):
        pass
    else:
        df=pd.DataFrame(
            {"Title":tuple(title_lst),
            "Price":tuple(price_lst)}
        )
        df.to_csv(env_vars.get('csv_path'),index=False,encoding='utf-8')
        print(df)

def df_to_mysql(title_lst,price_lst):
    # Set up the MySQL connection
    print(f'{env_vars['DB_USER']}')
    database_url = f"mysql+mysqlconnector://{env_vars['DB_USER']}:{env_vars['DB_PASSWORD']}@{env_vars['DB_HOST']}:{env_vars['DB_PORT']}/{env_vars['DB_NAME']}"
    engine = create_engine(database_url, echo=False)
    table_name = 'flipkart'
    if len(title_lst) != len(price_lst):
        pass
    else:
        df=pd.DataFrame(
            {"Title":tuple(title_lst),
            "Price":tuple(price_lst)}
        )
    # Store DataFrame in MySQL
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
