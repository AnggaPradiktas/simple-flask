from sqlite_db_select import select, insert

class Data:
    def get_data(self, query, values):
        return select(query, values)
    
    def insert_data(self, query, values):
        return insert(query, values)