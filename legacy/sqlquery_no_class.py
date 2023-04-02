'''
SQL queries I need
'''

from archivist import dosqlcode


tablename = 'inputs'


def createtable():
    sqlcreatetable = f'''CREATE TABLE IF NOT EXISTS {tablename} (
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


def droptable():
    sqldroptable = f'''DROP TABLE IF EXISTS {tablename}'''
    return dosqlcode(sqldroptable)


def addrow():
    sqladdrow = f'''INSERT INTO {tablename} (data, odometer, input_litres,
               fuel_consumption_displayed, fuel_consumption_real,
               photo, coordinates) VALUES (
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


def selectall():
    sqlselect = f'''SELECT * FROM {tablename};'''
    return dosqlcode(sqlselect)


def delrow():
    sqldelrow = f"""DELETE FROM {tablename} WHERE input_id = 5;"""
    return dosqlcode(sqldelrow)


def sqldelallrow():
    sqldelallrow = f'''DELETE FROM {tablename};'''
    return dosqlcode(sqldelallrow)
