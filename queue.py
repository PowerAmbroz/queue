# -*- coding: utf-8 -*-
import Queue
from threading import Thread

# tworzy przykład
z = Queue.LifoQueue() #LIFO- Last in first out; czyli liczby pokazują się od największej
#FIFO- First in first out



# dodaje pozycje do kolejki
for i in range(0,22,2): #range przyjmuje 3 argumenty z czego 2 są opcjonalne.
    #Argumentami są start, stop i step. Start rozpoczyna działanie, stop zatrzymuje a
    #step mówi co ile będzie skakać inkrementacja lub dekrementacja for i in range (1,10,2) Wynik: 1, 3, 5, 7, 9
    z.put(i) #elementy są dodawane na koniec kolejki (get() usuwa z koleji)
 
    
def dane_z_kolejki():
    while not z.empty(): # sprawdza czy kolejka nie jest pusta
        print z.get() # wypisuje element z kolejki na ekran
        z.task_done() # określa czy element się wykonał
        
for i in range(1): # zasięg ilości liczb w jednej linii
    t1 = Thread(target = dane_z_kolejki)
    t1.start() # start wątku

    
z.join() # działa z z.task_done
         # przede wszystkim z.join() utrzymuje rozmiar koleji


