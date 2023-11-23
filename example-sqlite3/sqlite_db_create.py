import sqlite3
import pandas as pd
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('flask_api.db', check_same_thread=False)
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS KARYAWAN")

# Creating table
table = """ CREATE TABLE KARYAWAN (
            id INT NOT NULL PRIMARY KEY,
            nama VARCHAR(125) NOT NULL,
            pekerjaan VARCHAR(125),
            usia INT
        );"""


cursor_obj.execute(table)


cursor_obj.execute('''
          INSERT INTO KARYAWAN (id, nama, pekerjaan, usia)

                VALUES
                (1,'Galih','Wen Engineer', 27),
                (2,'Dina','QA', 25),
                (3,'Satya','DBA', 34)
          ''')

cursor_obj.execute('''
          SELECT
          *
          FROM KARYAWAN
          ''')


connection_obj.commit()

df = pd.DataFrame(cursor_obj.fetchall(), columns=['id', 'nama', 'pekerjaan', 'usia'])
print (df)