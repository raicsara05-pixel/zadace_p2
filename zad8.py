'''
Funkciju iz prethodne zadaće učitati kao funkciju modula 
u novi program i pozvati je nakon traženja unosa od korisnika.
'''

#moj_modul.py (prethodna zadaca)
'''
def sa_zada(s):
    if len(s) == 0:
        return s
    else:
        return sa_zada(s[1:]) + s[0]
'''

  #glavni_program.py
import moj_modul

korisnicki_unos = input("Unesite string: ")

rezultat = moj_modul.sa_zada(korisnicki_unos)
print("Rezultat:", rezultat)
