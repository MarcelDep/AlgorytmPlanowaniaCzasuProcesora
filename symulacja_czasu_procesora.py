from generatordanych import eksperyment1, eksperyment2, eksperyment3, eksperyment4, eksperyment5
from algorytmy import FCFS, LCFS, SJF
def symulacja_planowania_czasu_procesora(procesy_do_wykonania, algorytm_planowania):
    ilosc_wykonanych_procesow = 0
    czas_do_konca_aktualnego_procesu = 0
    czas = 0
    czas_oczekiwania = 0
    ilosc_procesow_do_wykonania = len(procesy_do_wykonania)
    while True:
        # z każdym przejściem pętli zwiększamy czas o 1
        czas += 1
        #procesy będą trafiały do kolejki wtedy kiedy czas_nadejscia procesów do wykonania będzie mniejszy lub równy obecnemu czasowi
        procesy_w_kolejce = [[indeks, proces] for indeks, proces in enumerate(procesy_do_wykonania) if proces[0] <= czas]
        #jeżeli ilość procesów w kolejce jest większa niż 0 (istnieją jakieś procesy w kolejce) i czas do konca aktualnego procesu jest równy 0
        #(skończyliśmy wykonywać dany proces) to usuwamy ten z naszej kolejki i wykonujemy go przez czas równy czasowi wykonania procesu
        if len(procesy_w_kolejce) > 0 and czas_do_konca_aktualnego_procesu == 0:
            #w zależności od algorytmu planowania, wybieramy z kolejki proces który mamy usunąć
            indeks, proces_do_wykonania = algorytm_planowania(procesy_w_kolejce)
            procesy_do_wykonania.pop(indeks)
            #zwiększamy ilość wykonanych procesów o 1 za każdym razem gdy wykonamy jakiś proces (czas_do_konca_aktualnego_procesu == 0)
            ilosc_wykonanych_procesow += 1
            #czas oczekiwania na procesy liczymy jako różnicę obecnego czasu z czasem nadejścia obecnego procesu
            czas_oczekiwania += czas - proces_do_wykonania[1][0]
            czas_oczekiwania_procesu = czas - proces_do_wykonania[1][0]
            print(czas_oczekiwania_procesu)
            #po usunięciu procesu z kolejki, jako czas trwania procesu ustawiamy czas wykonania usuniętego procesu
            czas_do_konca_aktualnego_procesu = proces_do_wykonania[1][1]
        #jeżeli ilość wykonanych procesów jest równa ilości procesów do wykonania i czas wykonywania się pętli dla ostatniego procesu jest równy 0 to kończymy symulacja
        if ilosc_wykonanych_procesow == ilosc_procesow_do_wykonania and czas_do_konca_aktualnego_procesu == 0:
            print("Czas wykonania wszystkich procesów:", czas, "jednostek czasu.")
            print("Czas oczekiwania wszystkich procesów:", (czas_oczekiwania), "jednostek czasu.")
            #print("Średni czas oczekiwania wszystkich procesów:", (czas_oczekiwania / ilosc_wykonanych_procesow), "jednostek czasu.")
            return czas
        #jeżeli czas do końca aktualnego procesu jest większy od zera (proces nadal się wykonuje) to zmiejszamy ten czas o 1 z każdym przejściem pętli
        if czas_do_konca_aktualnego_procesu > 0:
            czas_do_konca_aktualnego_procesu -= 1

x = eksperyment1(150)
print("Scenariusz pierwszy - duże czasy nadejścia i krótkie czasy wykonania.")
print("_________________________________________________________________________________")
print('')
print("- Wyniki symulacji dla algorytmu FCFS:")
symulacja_planowania_czasu_procesora(x, FCFS)
# print("- Wyniki symulacji dla algorytmu LCFS:")
# symulacja_planowania_czasu_procesora(x, LCFS)
# print("- Wyniki symulacji dla algorytmu SJF:")
# symulacja_planowania_czasu_procesora(x, SJF)

#y = eksperyment2(150)
# print("Scenariusz drugi - krótkie czasy nadejścia i duże czasy wykonania.")
# print("_________________________________________________________________________________")
# print('')
#print("- Wyniki symulacji dla algorytmu FCFS")
#symulacja_planowania_czasu_procesora(y, FCFS)
#print("- Wyniki symulacji dla algorytmu LCFS")
#symulacja_planowania_czasu_procesora(y, LCFS)
#print("- Wyniki symulacji dla algorytmu SJF")
#symulacja_planowania_czasu_procesora(y, SJF)

# z = eksperyment3(150)
# print("Scenraiusz trzeci - zarówno krótkie czasy nadejścia jak i krótkie czasy wykonania")
# print("_________________________________________________________________________________")
# print('')
#print("- Wyniki symulacji dla algorytmu FCFS")
#symulacja_planowania_czasu_procesora(z, FCFS)
#print("- Wyniki symulacji dla algorytmu LCFS")
#symulacja_planowania_czasu_procesora(z, LCFS)
#print("- Wyniki symulacji dla algorytmu SJF")
#symulacja_planowania_czasu_procesora(z, SJF)
#
# a = eksperyment4(150)
# print("Scenraiusz czwarty - zarówno długie czasy nadejścia jak i długie czasy wykonania:")
# print("_________________________________________________________________________________")
# print('')
#print("- Wyniki symulacji dla algorytmu FCFS:")
#symulacja_planowania_czasu_procesora(a, FCFS)
#print("- Wyniki symulacji dla algorytmu LCFS:")
#symulacja_planowania_czasu_procesora(a, LCFS)
#print("- Wyniki symulacji dla algorytmu SJF:")
#symulacja_planowania_czasu_procesora(a, SJF)

# b = eksperyment5(150)
# print("Scenraiusz piąty - duży zakres czasów nadejścia i wykonania:")
# print("_________________________________________________________________________________")
# print('')
# #print("- Wyniki symulacji dla algorytmu FCFS:")
# #symulacja_planowania_czasu_procesora(b, FCFS)
# #rint("- Wyniki symulacji dla algorytmu LCFS:")
# #symulacja_planowania_czasu_procesora(b, LCFS)
# print("- Wyniki symulacji dla algorytmu SJF:")
# symulacja_planowania_czasu_procesora(b, SJF)