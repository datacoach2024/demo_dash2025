import json
import pandas as pd
from sqlalchemy import text

from connect import set_connection

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

create_tables()