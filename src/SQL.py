#!/usr/bin/env python
# coding: utf-8

import pymysql
import sqlalchemy as alch 
from getpass import getpass
import pandas as pd

import os
from dotenv import load_dotenv

def query_2023(table,engine):
    df=pd.read_sql_query(f""" SELECT * FROM {table}
    WHERE year>2022""", engine).drop(columns=['index'])
    return df

def to_sql(df, table, engine):
    df.to_sql(f'{table}', engine, if_exists='replace',index=True)
    return

def drop_opinion(table,engine):
    df=pd.read_sql_query(f"""SELECT * FROM {table} 
                         WHERE title NOT REGEXP 'Opinion';""",engine).drop(columns=['index'])
    return df

def uploading_to_sql(df, table, engine):
    df.to_sql(table,engine, if_exists='replace',index=True)
    return 

