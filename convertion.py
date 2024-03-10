import pandas as pd
from functions.mysoup import env_vars
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