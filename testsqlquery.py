'''
SQL queries I need based on testarchivist.
'''

import testarchivist
from decorators import try_except


class TestTableManager:
    def __init__(self, table: str = 'inputs') -> None:
        self.tablename = table
        self.whoisagoodboy = 'You are a good boy!'
        self.arch_obj = testarchivist.SQLArchivist()

    def __repr__(self) -> str:
        return f'TestTableManager for this table: "{self.tablename}"'

    @try_except
    def create_table(self) -> None:
        """Create a predefined table"""
        sqlcreatetable = f'''CREATE TABLE IF NOT EXISTS {self.tablename} (
        input_id INTEGER PRIMARY KEY,
        data REAL,
        odometer INTEGER,
        input_litres REAL,
        fuel_consumption_displayed REAL,
        fuel_consumption_real REAL,
        photo TEXT,
        coordinates TEXT
        );
        '''
        self.arch_obj.dosqlcode(sqlcreatetable)

    @try_except
    def drop_table(self) -> None:
        """Drop the table"""
        sqldroptable = f'''DROP TABLE IF EXISTS {self.tablename}'''
        self.arch_obj.dosqlcode(sqldroptable)

    @try_except
    def add_row(self, data: float = 1680453776.0000000,
                odometer: int = 0,
                input_litres: float = 0,
                fuel_consumption_displayed: float = 0,
                fuel_consumption_real: float = 0,
                photo: str = 'No',
                coordinates: str = 'Nowhere') -> None:
        """Add one row, defined or default"""
        sqladdrow = f'''INSERT INTO {self.tablename} (data, odometer,
                        input_litres, fuel_consumption_displayed,
                        fuel_consumption_real, photo, coordinates) VALUES (
                            {data},
                            {odometer},
                            {input_litres},
                            {fuel_consumption_displayed},
                            {fuel_consumption_real},
                            "{photo}",
                            '{coordinates}'
                            );
                    '''
        self.arch_obj.dosqlcode(sqladdrow)

    @try_except
    def select_all(self) -> list:
        """Select all rows from table; return list of tuples"""
        sqlselect = f'''SELECT * FROM {self.tablename};'''
        return self.arch_obj.dosqlcode(sqlselect)

    @try_except
    def del_row(self, k: int = 0) -> None:
        """Delete the specified row from table; default row=0 i.e. do nothing"""
        sqldelrow = f"""DELETE FROM {self.tablename} WHERE input_id = {k};"""
        self.arch_obj.dosqlcode(sqldelrow)

    @try_except
    def del_all_row(self) -> None:
        """Delete all rows, i.e. clear the table"""
        sqldelallrow = f'''DELETE FROM {self.tablename};'''
        self.arch_obj.dosqlcode(sqldelallrow)

    @try_except
    def custom_sql_query(self, sql_query) -> list:
        """Send your own SQL query; return fetch all list"""
        sql_query = sql_query
        return self.arch_obj.dosqlcode(sql_query)

    @try_except
    def select_last(self) -> tuple:
        """Select row of last record. Same as select_max for now."""
        sqlselect = f'''SELECT * FROM {self.tablename}
                        ORDER BY input_id DESC LIMIT 1;
                    '''
        return self.arch_obj.dosqlcodefetchone(sqlselect)

    @try_except
    def select_max(self) -> tuple:
        """Select row of last record. Same as select_last for now."""
        sqlselect = f'''SELECT * FROM {self.tablename}
                        WHERE input_id = (SELECT MAX(input_id)
                        FROM {self.tablename});
                    '''
        return self.arch_obj.dosqlcodefetchone(sqlselect)
