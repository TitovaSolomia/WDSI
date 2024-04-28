import webbrowser
import pandas as pd
from file_management.convertation import dataframeToPdf, xlsxToDataFrame


def generateFirstLevelPdf(order_size, order_time, tent_time, supplies_stock, assembling_time, component):
    firstLevelAnalisePerform(order_size, order_time, tent_time, supplies_stock, assembling_time, component)

    file_path = component+".xlsx"  
    data_frame = xlsxToDataFrame(file_path)

    if data_frame is not None:
        print("DataFrame created successfully!")
        print(data_frame.head()) 
    else:
        print("Failed to create DataFrame.")

    file_path = "analise1.pdf"
    dataframeToPdf(data_frame, file_path)

    if file_path:
        webbrowser.open(file_path)


def firstLevelAnalisePerform(order_size,order_time, tent_time, supplies_stock,assembling_time,component):
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
