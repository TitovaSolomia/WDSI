import pandas as pd

def record(order_size,order_time,supplies_stock,ordering_time, component, assembling_time):

    weeks = []
    for i in range(order_time):
        weeks.append(i+1)

    level = 2

    record = []

    for i in range(1,order_time+1):
        if i == 1:
            record.append(level)
        elif i == 2:
            record.append(component)
        else:
            record.append(0)
    
    #TU BEDZIE ZABAWA GDYZ- W ZALEZNOSCI OD PRZEDMIOTU POTRZEBUJEMY ROZNA ILOSC XD 
    #A ZATEM KLANIA SIE CHYBA SLOWNIK

    amount = {
        "ropes": 6,
        "waterproof_material": 1, 
        "floor_material": 1, 
        "tubes": 5, 
        "herrings": 8, 
        "net": 1, 
        "lock": 1
    }

    brutto = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time-assembling_time:
            brutto.append(0)
        elif i == order_time-tent_time-assembling_time:
            brutto.append(order_size*amount[f"{component}"])   #chyba giit  
                                            
    stock = []
    for i in range(1,order_time+1):
        if i <= order_time-tent_time-assembling_time:
            stock.append(supplies_stock)
        if i > order_time-tent_time-assembling_time:
            if order_size*amount[f"{component}"]>=supplies_stock:
                stock.append(0)                                            
            elif order_size*amount[f"{component}"]<supplies_stock:
                stock.append(supplies_stock-order_size*amount[f"{component}"])     #tu tez powinno byc giit

    netto = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time-assembling_time:
            netto.append(0)
        elif i == order_time-tent_time-assembling_time:
            if order_size*amount[f"{component}"]- supplies_stock>= 0:
                netto.append(order_size*amount[f"{component}"]-supplies_stock)
            else:
                netto.append(0)               #potrzeba netto nie może być liczbą ujemną!

    order = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time-assembling_time-ordering_time:
            order.append(0)
        elif i == order_time-tent_time-assembling_time-ordering_time:
            if order_size*amount[f"{component}"]-supplies_stock>=0:
                order.append(order_size*amount[f"{component}"]-supplies_stock)
            else:
                order.append(0)

    pickup = []
    for i in range(1,order_time+1):
        if i != order_time-tent_time-assembling_time:
            pickup.append(0)
        elif i == order_time-tent_time-assembling_time:
            pickup.append(order_size*amount[f"{component}"])

    # dane
    dane = {
        'Level': record,
        'Week': weeks,
        'BRUTTO': brutto,
        'Supplies stock': stock,
        'NETTO': netto,
        'Order': order,
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


components = ["ropes","waterproof_material", "floor_material", "tubes", "herrings", "net", "lock"]

for component in components:

    print(f"{component}")
    supplies_stock = int(input("Podaj wstępny zapas magazynu: \n"))                             #inny dla kazdej skladowej 
    ordering_time = int(input("Podaj czas (w tygodniach) potrzebny na zamówienie pojedynczego przedmiotu: \n"))
    assembling_time = int(input("Podaj czas (w tygodniach) potrzebny na złożenie większej części składowej z tego elementu: \n"))

    record(order_size,order_time,supplies_stock,ordering_time, component,assembling_time)

    print("Plik excel został utworzony pomyślnie.")