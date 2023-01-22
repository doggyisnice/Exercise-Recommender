import csv
import sqlite3 
from sqlite3 import Error
import pandas as pd
from pathlib import Path



# connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
# c = connection.cursor()
# c.execute('''
# CREATE TABLE exercise (
#     id INT, 
#     muscle_group TEXT,
#     exercise TEXT, 
#     level TEXT, 
#     u_l_c TEXT, 
#     p_p TEXT, 
#     modality TEXT, 
#     joint TEXT,
#     primary key(id)
#     )''')

connection =sqlite3.connect('/Users/joel/VSCODE/Exercise_recommender/data.db')
c = connection.cursor()

with open('exercise_list.csv') as file:
    no_records = 0
    for row in file:
        c.execute('INSERT INTO exercise VALUES (?,?,?,?,?,?,?,?)', row.split(","))
        no_records += 1

print(f"{no_records} Transferred")

connection.commit()
connection.close()
