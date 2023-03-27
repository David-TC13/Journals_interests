#!/usr/bin/env python
# coding: utf-8

import pymysql
import sqlalchemy as alch 
from getpass import getpass
import pandas as pd

import os
from dotenv import load_dotenv

def to_sql(df, table, engine):
    df.to_sql(f'{table}', engine, if_exists='append',index=False)
    return

def drop_opinion_year(table,engine):
    df=pd.read_sql_query(f"""SELECT DISTINCT * FROM {table}
                    WHERE title NOT REGEXP 'Opinion' and year>2022;""",engine)
    return df

def uploading_to_sql(df, table, engine):
    df.to_sql(f'{table}',engine, if_exists='append',index=False)
    return 


def replace_to_sql(df, table, engine):
    df.to_sql(f'{table}',engine, if_exists='replace',index=False)
    return 
