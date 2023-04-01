import archivist

# считать архив
archive = archivist.readjsonarchive()

add = {
        "data": "40.01.2023",
        "odometer": 401,
        "input_litres": 402,
        "fuel_consumption_displayed": 403.403,
        "fuel_consumption_real": 404.404,
        "photo": "http://40",
        "coordinates": "Анапа40"
    }

# добаваить словарь в конец архива
archivist.addtoarchive(add)
