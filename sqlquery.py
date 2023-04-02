'''
SQL queries I need.
'''

from archivist import dosqlcode
from decorators import try_except


class TableManager:
    def __init__(self, table: str = 'inputs') -> None:
        self.tablename = table
        self.whoisagoodboy = 'You are a good boy!'

    def __repr__(self) -> str:
        return f'TableManager for this table: "{self.tablename}"'

    @try_except
    def create_table(self):
        sqlcreatetable = f'''CREATE TABLE IF NOT EXISTS {self.tablename} (
        input_id INTEGER PRIMARY KEY,
        data INTEGER,
        odometer INTEGER,
        input_litres REAL,
        fuel_consumption_displayed REAL,
        fuel_consumption_real REAL,
        photo TEXT,
        coordinates TEXT
        );
        '''
        return dosqlcode(sqlcreatetable)

    @try_except
    def drop_table(self):
        sqldroptable = f'''DROP TABLE IF EXISTS {self.tablename}'''
        return dosqlcode(sqldroptable)

    @try_except
    def add_row(self):
        sqladdrow = f'''INSERT INTO {self.tablename} (data, odometer,
                        input_litres, fuel_consumption_displayed,
                        fuel_consumption_real, photo, coordinates) VALUES (
                            80012023,
                            801,
                            802,
                            803.803,
                            804.804,
                            'http://80',
                            'Анапа80'
                            );
                    '''
        return dosqlcode(sqladdrow)

    @try_except
    def select_all(self):
        sqlselect = f'''SELECT * FROM {self.tablename};'''
        return dosqlcode(sqlselect)

    @try_except
    def del_row(self, k: int = 0):
        sqldelrow = f"""DELETE FROM {self.tablename} WHERE input_id = {k};"""
        return dosqlcode(sqldelrow)

    @try_except
    def del_all_row(self):
        sqldelallrow = f'''DELETE FROM {self.tablename};'''
        return dosqlcode(sqldelallrow)
