import pandas as pd

def record(order_size,order_time,supplies_stock,assembling_time, component):

    weeks = []
    for i in range(order_time):
        weeks.append(i+1)

    level = 1

    record = []

    for i in range(1,order_time+1):
        if i == 1:
            record.append(level)
        elif i == 2:
            record.append(component)
        else:
            record.append(0)

    brutto = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time:
            brutto.append(0)
        elif i == order_time-tent_time:
            brutto.append(order_size)          #potrzebujemy po 1 z kazdych z tych elementow do jednego gotowego namiotu, stad liczba potrzebnych
                                               #produktow brutto rowna liczbie potrzebnego calego zamowienia
    stock = []
    for i in range(1,order_time+1):
        if i <= order_time-tent_time:
            stock.append(supplies_stock)
        if i > order_time-tent_time:
            if order_size>=supplies_stock:
                stock.append(0)
            elif order_size<supplies_stock:
                stock.append(supplies_stock-order_size)     

    netto = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time:
            netto.append(0)
        elif i == order_time-tent_time:
            if order_size- supplies_stock>= 0:
                netto.append(order_size-supplies_stock)
            else:
                netto.append(0)               #potrzeba netto nie może być liczbą ujemną!

    assembling = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time-assembling_time:
            assembling.append(0)
        elif i == order_time-tent_time-assembling_time:
            if order_size-supplies_stock>=0:
                assembling.append(order_size-supplies_stock)
            else:
                assembling.append(0)

    pickup = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time:
            pickup.append(0)
        elif i == order_time-tent_time:
            pickup.append(order_size)

    # dane
    dane = {
        'Level': record,
        'Week': weeks,
        'BRUTTO': brutto,
        'Supplies stock': stock,
        'NETTO': netto,
        'Assembling': assembling,
        'Pickup': pickup
    }

    # Tworzenie ramki danych
    df = pd.DataFrame(dane)

    # Tworzenie pliku Excel
    nazwa_pliku = f"{component}.xlsx"
    df.to_excel(nazwa_pliku, index=False)



order_size = int(input("Podaj wielkość zamówienia- ile namiotów potrzebujesz?\n"))
order_time = int(input("Podaj tydzień odbioru zamowienia (od dzis, liczba)\n"))
tent_time = int(input("Podaj czas (w tygodniach) potrzebny na złożenie namiotu z gotowych części: \n"))


components = ["roof","floor", "frame", "entry"]

for component in components:

    print(f"{component}")
    supplies_stock = int(input("Podaj wstępny zapas magazynu: \n"))                             #inny dla kazdej skladowej 
    assembling_time = int(input("Podaj czas (w tygodniach) potrzebny na złożenie pojedynczego przedmiotu: \n"))

    record(order_size,order_time,supplies_stock,assembling_time, component)

    print("Pliki excel zostały utworzone pomyślnie.")



# TRZEBA JESZCZE OGARNAC/ DOPISAC JAKIES WYJATKI GDY NP. CZAS ZLOZENIA NAMIOTU I CZAS SKLADANIA/ZAMAWIANIA POTRZEBNYCH CZESCI BYLBY WIEKSZY NIZ
# ZADEKLAROWANY CZAS ODBIORU !! (ORDER_TIME) (IF ...... <0
#                                              PRINT("WE'RE SORRY. WE ARE NOT ABLE TO MAKE YOUR ORDER IN THIS TIME- IT TAKES LONGER"))