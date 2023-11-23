import sqlite3
 
# Connecting to sqlite
connection_obj = sqlite3.connect('flask_api.db', check_same_thread=False)
 
# cursor object
cursor_obj = connection_obj.cursor()


def select(query, values):
   cursor_obj.execute(query, values)
   row_headers = [x[0] for x in cursor_obj.description]
   result = cursor_obj.fetchall()
   json_data = []
   for r in result:
      json_data.append(dict(zip(row_headers, r)))
   return json_data
      

def insert(query, values):
   cursor_obj.execute(query, values)
   connection_obj.commit()