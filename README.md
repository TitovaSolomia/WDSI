# WDSI

## Project makers:
Solomiia Titova ZIISS1-1213
Magdalena Wachowska ZIISS1-1213

### Homework- MRP system
Ważne uwagi:
- należy pobrać repozytorium na swój komputer (git clone + adres repozytorium)
- należy otworzyć folder wdsi2 w Visual Studio Code
- zaimportować odpowiednie biblioteki (pandas, openpyxl, flask, flask_cors, numpy, matplotlib.pyplot, webbrowser)
- następnie przed wyświetleniem strony należy URUCHOMIĆ KOD ZAWARTY W PLIKU "proccessQuantity.py" !! BARDZO WAŻNE, bez tego strona nie zadziała
- korzystając np. z rozszerzenia LiveServer należy wyświetlić stronę- plik "index.html"
- przechodzimy po kolei przez następne części na stronie- rozpoczynając od "Buy Now", przez sekcję "For Producent" - należy wypełnić wszystkie wymagane dane (ilości produktów i czasy **czas zawsze podajemy w tygodniach)
- po poprawnym uzupełnieniu danych (wpisując wartości dodatnie) wygenerowane zostaną po kolei pliki PDF z poszczególnymi rekordami MRP (tabelkami)

  *** Ilości poszczególnych elementów składających się na jeden gotowy namiot:
  - dach, podłoga, wejście, stelaż- 1 szt
  - sznurki - 6 szt
  - materiał wodoodporny, materiał podłogowy, siatka ochronna, zamek- 1 szt
  - rurki - 5 szt
  - śledzie - 8szt
    
#### Additional
Ze względu na to, że pojawiły się problemy z przekazaniem niektórych zmiennych wprowadzanych przez użytkownika na stronie, do kodu python do poziomu 2, poza folderem "wdsi2" zamieściłyśmy w tym repozytorium również plik "czysto pythonowy"- records.py
Działa on na praktycznie tym samym algorytmie, z taką różnicą, że nie mamy wizualnej strony, użytkownik musi wprowadzić dane w terminalu. Po poprawnym uzupełnieniu wygenerowane zostaną pliki .xlsx, osobno dla każdego elementu namiotu z rekordem mrp.
