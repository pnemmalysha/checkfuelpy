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
import time
import random

a = sqlquery.TableManager()
#b = sqlquery.TableManager('shittable')

def p():
    for i in a.select_all():
        print(i)

a.create_table()
a.add_row()
a.del_all_row()
a.del_row()
#a.drop_table()
a.select_all()
a.tablename

a.add_row(data = time.time(),
          odometer = 200055,
          input_litres = 34.12,
          fuel_consumption_displayed = 10.6,
          fuel_consumption_real = 13.4,
          photo = 'nofotohere',
          coordinates='Far Far Away 13',)

def random_row_gen(k=10):
    for i in range(k):
        a.add_row(data = time.time()+i*1000+random.randint(1,100),
                  odometer = 200055+i*100+random.randint(1,100),
                  input_litres = 25.0+random.randint(1,25),
                  fuel_consumption_displayed = 7+random.randint(1,100)/10,
                  fuel_consumption_real = 9+random.randint(1,100)/10,
                  photo = 'nofotohere'+str(random.randint(1,1000)),
                  coordinates='Far Far Away '+str(random.randint(1,1000)),)

random_row_gen()

p()