historyfilename = 'history.txt'

def ask_odometer():
    ok = 0
    while ok == 0:
        try:
            odometer = float(input('Текущий пробег: '))
            ok = 1
        except(ValueError):
            print('Нужно число')
    print('odometer', odometer)
    return(odometer)

def ask_input_litres():
    ok = 0
    while ok == 0:
        try:
            input_litres = float(input('Залито бензина (л): '))
            ok = 1
        except(ValueError):
            print('Нужно число')
    print('input_litres', input_litres)
    return(input_litres)

def ask_fuel_consumption_displayed():
    ok = 0
    while ok == 0:
        try:
            fuel_consumption_displayed = float(input('Расход по БК: '))
            ok = 1
        except(ValueError):
            print('Нужно число')
    print('fuel_consumption_displayed', fuel_consumption_displayed)
    return(fuel_consumption_displayed)

def calculate_mileage(odometer,previous_odometer):
    mileage = odometer - previous_odometer
    print('mileage', mileage)
    return(mileage)

def calculate_fuel_consumption_real(input_litres,mileage):
    fuel_consumption_real = (input_litres/mileage)*100
    print('fuel_consumption_real',fuel_consumption_real)
    return(fuel_consumption_real)

def history_read(historyfilename):
    with open (historyfilename, 'r') as historyfile:
        previous_history = historyfile.readlines()
        previous_history_oneliner = ''.join(previous_history)
        previous_odometer_raw = previous_history[0]
        previous_odometer = float(previous_odometer_raw.split()[1])
        return(previous_odometer,previous_history_oneliner)

def make_new_history(odometer,input_litres,fuel_consumption_real,fuel_consumption_displayed):
    new_history_oneliner = f'Пробег: {int(odometer)} км\nЗалито: {round(input_litres,2)} л\nРасход: {round(fuel_consumption_real,2)} л/100 км\nРасход по БК: {round(fuel_consumption_displayed,2)} л/100 км\n\n===\n\n'
    return(new_history_oneliner)

def sum_history(new_history_oneliner,previous_history_oneliner):
    full_history_oneliner = new_history_oneliner+previous_history_oneliner
    return(full_history_oneliner)

def history_write(historyfilename,full_history_oneliner):
    with open (historyfilename, 'w') as historyfile:
        historyfile.write(full_history_oneliner)

def main():
    odometer = ask_odometer()
    input_litres = ask_input_litres()
    fuel_consumption_displayed = ask_fuel_consumption_displayed()
    previous_odometer, previous_history_oneliner = history_read(historyfilename)
    mileage = calculate_mileage(odometer,previous_odometer)
    fuel_consumption_real = calculate_fuel_consumption_real(input_litres,mileage)
    new_history_oneliner = make_new_history(odometer,input_litres,fuel_consumption_real,fuel_consumption_displayed)
    full_history_oneliner = sum_history(new_history_oneliner,previous_history_oneliner)
    history_write(historyfilename,full_history_oneliner)

if __name__ == '__main__':
    main()