import random
SEED = 1
random.seed(SEED)
def eksperyment1(number):
    """Generator danych dla eksperymentu pierwszego - duże czasy nadejścia i krótkie czasy wykonania."""
    lista_procesow1 = []
    # Dodajemy czas nadejscia do kazdego procesu od 1 do wpisanej liczby
    for i in range(1, number + 1):
        # Generujemy lososwy długi czas nadejścia z przedziału od 100 do 125
        czas_nadejscia1 = random.randint(100, 125)
        # Generujemy lososwy krótki czas wykonania z przedziału od 5 do 10
        czas_wykonania1 = random.randint(5, 10)
        lista = [czas_nadejscia1, czas_wykonania1]
        lista_procesow1.append(lista)
        lista_procesow1.sort(key=lambda x: x[0])
    print('')
    print("_________________________________________________________________________________")
    print('Lista procesów dla eksperymentu pierwszego', lista_procesow1)
    return lista_procesow1

def eksperyment2(number):
    """Generator danych dla eksperymentu drugiego - krótkie czasy nadejścia i duże czasy wykonania."""
    lista_procesow2 = []
    #dodajemy czas nadejscia i czas wykonania do kazdego procesu od 1 do wpisanej liczby
    for i in range(1, number+1):
        #generujemy lososwy krótki czas nadejścia z przedziału od 5 do 10
        czas_nadejscia2 = random.randint(5, 10)
        #generujemy lososwy długi czas wykonania z przedziału od 100 do 125
        czas_wykonania2 = random.randint(100, 125)
        lista = [czas_nadejscia2, czas_wykonania2]
        lista_procesow2.append(lista)
        lista_procesow2.sort(key=lambda x: x[0])
    print('')
    print("_________________________________________________________________________________")
    print('Lista procesów dla eksperymentu drugiego', lista_procesow2)
    return lista_procesow2

def eksperyment3(number):
    """Generator danych dla eksperymentu trzeciego - zarówno krótkie czasy nadejścia jak i krótkie czasy wykonania"""
    lista_procesow3 = []
    #dodajemy czas nadejscia i czas wykonania do kazdego procesu od 1 do wpisanej liczby
    for i in range(1, number+1):
        #generujemy lososwy krótki czas nadejścia z przedziału od 5 do 15
        czas_nadejscia3 = random.randint(5, 15)
        #generujemy lososwy krótki czas wykonania z przedziału od 5 do 15
        czas_wykonania3 = random.randint(5, 15)
        lista = [czas_nadejscia3, czas_wykonania3]
        lista_procesow3.append(lista)
        lista_procesow3.sort(key=lambda x: x[0])
    print('')
    print("_________________________________________________________________________________")
    print('Lista procesów dla eksperymentu trzeciego', lista_procesow3)
    return lista_procesow3

def eksperyment4(number):
    """Generator danych dla eksperymentu czwartego - zarówno długie czasy nadejścia jak i długie czasy wykonania"""
    lista_procesow4 = []
    # dodajemy czas nadejscia i czas wykonania do kazdego procesu od 1 do wpisanej liczby
    for i in range(1, number + 1):
        # generujemy lososwy duży czas nadejścia z przedziału od 100 do 125
        czas_nadejscia4 = random.randint(100, 125)
        # generujemy lososwy krótki czas wykonania z przedziału od 100 do 125
        czas_wykonania4 = random.randint(100, 125)
        lista = [czas_nadejscia4, czas_wykonania4]
        lista_procesow4.append(lista)
        lista_procesow4.sort(key=lambda x: x[0])
    print('')
    print("_________________________________________________________________________________")
    print('Lista procesów dla eksperymentu czwartego', lista_procesow4)
    return lista_procesow4

def eksperyment5(number):
    """Generator danych dla eksperymentu piątego - duży zakres czasów nadejścia i wykonania"""
    lista_procesow5 = []
    # dodajemy czas nadejscia i czas wykonania do kazdego procesu od 1 do wpisanej liczby
    for i in range(1, number + 1):
        # generujemy lososwy czas nadejścia z przedziału od 1 do 100
        czas_nadejscia5 = random.randint(1, 100)
        # generujemy lososwy czas wykonania z przedziału od 1 do 100
        czas_wykonania5 = random.randint(1, 100)
        lista = [czas_nadejscia5, czas_wykonania5]
        lista_procesow5.append(lista)
        lista_procesow5.sort(key=lambda x: x[0])
    print('')
    print("_________________________________________________________________________________")
    print('Lista procesów dla eksperymentu piątego', lista_procesow5)
    return lista_procesow5