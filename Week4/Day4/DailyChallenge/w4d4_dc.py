import psycopg2
import requests
import random

connection = psycopg2.connect(host='localhost', user='postgres', password='mandolintheyanks6', dbname='w4d4_dc')
cursor = connection.cursor()
create_query = "CREATE TABLE countries (" \
               "name VARCHAR(50)," \
               "capital VARCHAR(50)," \
               "flag VARCHAR(50)," \
               "subregion VARCHAR(50)," \
               "population INTEGER)"
# cursor.execute(create_query)
# connection.commit()

response = requests.get('https://restcountries.com/v3.1/all')
response.raise_for_status()
response_json = response.json()

for i in range(10):
    choice = random.choice(response_json)
    name = choice['name']['official'].replace("'","")
    capital = choice['capital'][0].replace("'","")
    flag = choice['flags']['png']
    subregion = choice['subregion'].replace("'","")
    population =  choice['population']
    query = f"INSERT INTO countries (name, capital, flag, subregion, population)" \
            f"VALUES ('{name}', '{capital}', '{flag}', '{subregion}', '{population}');"
    cursor.execute(query)
    connection.commit()