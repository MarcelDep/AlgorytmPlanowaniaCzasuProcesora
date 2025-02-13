def FCFS(procesy_w_kolejce):
    #tworzymy listę w której umieszczamy czasy nadejścia, czasy wykonania każdego procesu, indeks informujący o miejscu w kolejce
    #dodając do tego jego indeks który będzie służył do identyfikacji procesy potrzebnego do usunięcia z listy procesów
    czasy_wejscia = [[indeks, proces] for indeks, proces in enumerate(procesy_w_kolejce)]
    #z listy procesów wybieramy ten który jako pierwszy został umieszczony w liście (najmniejszy indeks na pozycji [1][0] bo z listy
    #[indeks, [indeks, [czas_nadejścia, czas_wykonania]]], patrzymy na drugi element [1], dalej na pierwszy
    #element [0], czyli indeks informujący o momencie w którym proces traił do kolejki)
    indeks, najmniejszy_czas_przyjscia = min(czasy_wejscia, key=lambda x: x[1][0])
    return indeks, najmniejszy_czas_przyjscia
def LCFS(procesy_w_kolejce):
    czasy_wejscia = [[indeks, proces] for indeks, proces in enumerate(procesy_w_kolejce)]
    # z listy procesów wybieramy ten który jako ostatni został umieszczony w liście (największy indeks na pozycji [1][0] bo z listy
    # [indeks, [czas_nadejścia, czas_wykonania]], patrzymy na drugi element [1], dalej na pierwszy
    # element [0], czyli indeks informujący o momencie w którym proces traił do kolejki)
    indeks, najwiekszy_czas_przyjscia = max(czasy_wejscia, key=lambda x: x[1][0])
    return indeks, najwiekszy_czas_przyjscia
def SJF(procesy_w_kolejce):
    czasy_wejscia = [[indeks, proces] for indeks, proces in enumerate(procesy_w_kolejce)]
    # z listy procesów wybieramy ten który ma najmniejszy czas wykonania (najmniejsza wartość na pozycji [1][1][1] bo z listy
    # [indeks, [indeks,[czas_nadejścia, czas_wykonania]]] patrzymy na listę o indeksie [1], w niej na listę czasów o indeksie [1][1]
    # a z tej listy na czas_wykonania o indeksie [1][1][1]
    indeks, najmniejszy_czas_wykonania = min(czasy_wejscia, key=lambda x: x[1][1][1])
    return indeks, najmniejszy_czas_wykonania