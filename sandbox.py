"""
Just a test sandbox for experiments.
"""

# считать архив JSON
import archivist

archive = archivist.readjsonarchive()

add = {
        "data": "60.01.2023",
        "odometer": 601,
        "input_litres": 602,
        "fuel_consumption_displayed": 603.603,
        "fuel_consumption_real": 604.604,
        "photo": "http://60",
        "coordinates": "Анапа60"
    }

# добаваить словарь в конец архива JSON
archivist.addtoarchive(add)


# вывести все строки из архива SQLite
import sqlquery_no_class

_ = [print(row) for row in sqlquery_no_class.selectall()]


x = sqlquery_no_class.createtable()
x = sqlquery_no_class.addrow()
x = sqlquery_no_class.selectall()
x = sqlquery_no_class.delrow()
x = sqlquery_no_class.sqldelallrow()
x = sqlquery_no_class.droptable()


# Создаю экземпляр класса TableManager и делаю всё как царь
import sqlquery
from importlib import reload
import time
import random

a = sqlquery.TableManager()
#b = sqlquery.TableManager('shittable')

def p():
    for i in a.select_all():
        print(i)
        #print(time.ctime(i[1]))

#a.drop_table()
a.create_table()
a.add_row()
a.del_all_row()
a.del_row()
a.select_all()
a.tablename

a.add_row(data = time.time(),
          odometer = 200000,
          input_litres = 34.12,
          fuel_consumption_displayed = 10.6,
          fuel_consumption_real = 13.4,
          photo = 'nofotohere',
          coordinates='Far Far Away 13',)

def random_row_gen(k=10):
    for i in range(k):
        a.add_row(data = time.time()+i*864000+random.randint(1,864000),
                  odometer = 200055+i*250+random.randint(-100,100),
                  input_litres = 25.0+random.randint(-15,25),
                  fuel_consumption_displayed = 7+random.randint(1,100)/10,
                  fuel_consumption_real = 9+random.randint(1,100)/10,
                  photo = 'nofotohere'+str(random.randint(1,1000)),
                  coordinates='Far Far Away '+str(random.randint(1,10)),)

random_row_gen()

p()

reload(sqlquery)

max_row = a.select_last()




# Создаю экземпляр класса TestTableManager и делаю всё как в тумане
from testsqlquery import TestTableManager
b = TestTableManager()
def pp():
    for i in b.select_all():
        print(i)
        #print(time.ctime(i[1]))

pp()

b.del_row(7)
b.create_table()
b.add_row()
b.del_all_row()
b.del_row()
b.select_all()
b.select_last()
b.select_max()
b.del_row()

b.add_row(data = time.time(),
          odometer = 200000,
          input_litres = 34.12,
          fuel_consumption_displayed = 10.6,
          fuel_consumption_real = 13.4,
          photo = 'nofotohere',
          coordinates='Far Far Away 13',)

def random_row_gen(k=10):
    for i in range(k):
        b.add_row(data = time.time()+i*864000+random.randint(1,864000),
                  odometer = 200055+i*250+random.randint(-100,100),
                  input_litres = 25.0+random.randint(-15,25),
                  fuel_consumption_displayed = 7+random.randint(1,100)/10,
                  fuel_consumption_real = 9+random.randint(1,100)/10,
                  photo = 'nofotohere'+str(random.randint(1,1000)),
                  coordinates='Far Far Away '+str(random.randint(1,10)),)
