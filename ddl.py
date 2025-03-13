import json
import pandas as pd
from sqlalchemy import text

from connect import set_connection

SCHEMA = "demo_dash"

def create_tables():
    try:
        # читаем содержимое файла 'queries/tables.sql'
        with open('queries/tables.sql') as f:
            tables_query = f.read()
        
        # создаём схему и таблицы
        with set_connection() as psg:
            psg.execute(text(tables_query))
            psg.commit()
        
        print("Tables created successfully")
    except Exception as e:
        print(e)



def read_xl(sheet_name, columns_dict):
    temp_df = pd.read_excel(
        'source/adventure_works.xlsx',
        sheet_name=sheet_name,
        usecols=columns_dict.keys()
    ).rename(columns=columns_dict)
    return temp_df


with open('tables.json') as f:
    tables_dict = json.load(f) 


def insert_to_db(temp_df, tbl_name):
    with set_connection() as psg:
        temp_df.to_sql(
            schema=SCHEMA,
            name=tbl_name,
            con=psg,
            index=False,
            if_exists='replace'
        )


def create_views():
    with open('queries/views.sql') as f:
        views = f.read()

    with set_connection() as psg:
        psg.execute(text(views))
        psg.commit()

    print("Views were successfully created")


def xl_etl(sheet_name, columns_dict, tbl_name):
    print(f"inserting data to {tbl_name}...")
    temp_df = read_xl(sheet_name, columns_dict)
    insert_to_db(temp_df, tbl_name)

def create_n_insert():    
    try:
        print('try entrypoint')
        with set_connection() as psg:
            psg.execute(text("select 1 from demo_dash.sales"))
    except:
        print('except entrypoint')
        for k, v in tables_dict.items():
            xl_etl(k, v["columns"], v["table_name"])
    
    create_views()

create_n_insert()

