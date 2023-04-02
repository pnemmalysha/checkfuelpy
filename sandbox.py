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

a = sqlquery.TableManager('shittable')

a.create_table()
a.add_row()
a.del_all_row()
a.del_row()
a.drop_table()
a.select_all()
a.tablename

a.del_row()
for i in a.select_all():
    print(i)