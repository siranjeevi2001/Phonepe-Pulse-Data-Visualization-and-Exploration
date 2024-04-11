

import mysql.connector
import pandas as pd

import mysql.connector
import pandas as pd


def retrieve_transaction_data():
    # Establish the database connection
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database='phonepe'
    )

    # Create a cursor object
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM agg_transaction")
    data = cursor.fetchall()
    df = pd.DataFrame(data,columns=['State', 'Year', 'Quarter', 'Transaction_Type', 'Transaction_Count', 'Transaction_Amount'],index=None)
    cursor.close()
    db_connection.close()
    return df





def retrieve_transaction_map():
    # Establish the database connection
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database='phonepe'
    )

    # Create a cursor object
    cursor = db_connection.cursor()
    cursor.execute("SELECT State, Transaction_Count,Transaction_Amount FROM agg_transaction GROUP BY State ")
    data = cursor.fetchall()
    df = pd.DataFrame(data,columns=['State','Transaction_Count', 'Transaction_Amount'],index=None)
    
    a = df['State']
    b = a.unique()
    df1 = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
    c = df1['state']
    d = c.unique()
    for i, j in zip(b, d):
        df['State'] = df['State'].replace(f"{i}", f"{j}")
        
    cursor.close()
    db_connection.close()
    
    return df


def map():
    df = retrieve_transaction_map()
    a = df['State']
    b = a.unique()
    df1 = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
    c = df1['state']
    d = c.unique()
    for i, j in zip(b, d):
        df['State'] = df['State'].replace(f"{i}", f"{j}")
    return df


def map_year():
    df = retrieve_transaction_data()
    a = df['State']
    b = a.unique()
    df1 = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")
    c = df1['state']
    d = c.unique()
    for i, j in zip(b, d):
        df['State'] = df['State'].replace(f"{i}", f"{j}")
    return df



# --------------------------Agge _user-----------------------------------

def retrieve_agg_user():
    # Establish the database connection
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database='phonepe'
    )

    # Create a cursor object
    cursor = db_connection.cursor()

    # Define the function to retrieve transaction data

    cursor.execute(f"SELECT * FROM agg_user")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Brand_type', 'Users_count', 'Quarter', 'State', 'Year', 'Percentage'])
    cursor.close()
    
    return df