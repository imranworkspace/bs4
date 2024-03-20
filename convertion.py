import pandas as pd
from functions.mysoup import env_vars
from sqlalchemy import create_engine
def my_credentials():
    database_url = f"mysql+mysqlconnector://{env_vars['DB_USER']}:{env_vars['DB_PASSWORD']}@{env_vars['DB_HOST']}:{env_vars['DB_PORT']}/{env_vars['DB_NAME']}"
    engine = create_engine(database_url, echo=False)
    return engine
def mydf(payload):
    df = pd.DataFrame.from_dict(payload, orient='index')
    # starting index 1 instead of 0
    df.index = range(1,len(df)+1)
    # Rename the index and columns using a dictionary
    df.rename_axis("myindex")
    df = df.rename(columns={'arg1': env_vars.get('ID_COLUMN_NAME2'),
                            'arg2': env_vars.get('ID_COLUMN_NAME3')
                            })
    return df
def categories_data_from_args(args):
    payload = {}
    # Iterate over each argument
    for arg_index, arg in enumerate(args,start=0):
        # Iterate over each value in the argument
        for value_index, value in enumerate(arg):
            # Check if the category already exists in the dictionary
            if value_index not in payload:
                payload[value_index] = {}
            # Add the value to the corresponding category
            payload[value_index][f'arg{arg_index+1}'] = value
    return payload
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

#  using panda this is for direct into mysql without model
def df_to_mysql(*args):
    # Set up the MySQL connection
    table_name = env_vars.get('TABLE_NAME')
    print(table_name)
    if table_name=='':
        print('table does not found')
    if len(args)==0:
        print(env_vars.get('EMPTY_RESULTSET'))
    else:
        payload = categories_data_from_args(args)
        df=mydf(payload)
        engine = my_credentials()
        # Store DataFrame in MySQL
        try:
            df.to_sql(table_name, con=engine, if_exists="replace", index=True)
            print("Data inserted successfully into MySQL table:", table_name)
        except Exception as e:
            print("Error occurred while inserting data into MySQL table:", e)

def df_to_xml(*args):
    if len(args)==0:
        print(env_vars.get('EMPTY_RESULTSET'))
    else:
        payload = categories_data_from_args(args)
        df=mydf(payload)
        df.columns = df.columns.str.replace(' ', '_')
        try:
            # Convert DataFrame to XML
            xml_output = df.to_xml(index=False, root_name='Laptops', row_name='Laptop')
            # Write XML to a file with UTF-8 encoding
            with open("laptops.xml", "w", encoding="utf-8") as f:
                f.write(xml_output)
            print("Data inserted successfully into xml ")
        except Exception as e:
            print("Error occurred while inserting data into xml ", e)

def df_to_excel(*args):
    if len(args)==0:
        print(env_vars.get('EMPTY_RESULTSET'))
    else:
        payload = categories_data_from_args(args)
        df=mydf(payload)
        df.columns = df.columns.str.replace(' ', '_')
        try:
            # Convert DataFrame to XML
            # Write DataFrame to Excel file
            df.to_excel("laptops.xlsx", index=False)
            print("Data inserted successfully into excel ")
        except Exception as e:
            print("Error occurred while inserting data into excel ", e)
