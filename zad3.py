'''
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 

Nedovoljan
0-49%

Dovoljan
50-65%

Dobar
65-80%

Vrlodobar
80-90%

Izvrstan
90-100%
'''

import csv

studenti = []

with open("rezultati.csv", "r", encoding="utf-8") as datoteka:
    citac = csv.reader(datoteka)
    for redak in citac:
        ime = redak[0]
        prezime = redak[1]
        bodovi = int(redak[2])
        studenti.append((ime, prezime, bodovi))

n = len(studenti)
for i in range(n):
    for j in range(0, n - i - 1):
        # student[1] je prezime
        if studenti[j][1] > studenti[j + 1][1]:
            privremena = studenti[j]
            studenti[j] = studenti[j + 1]
            studenti[j + 1] = privremena

rjecnik_rangova = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlodobar": 0,
    "Izvrstan": 0
}

for student in studenti:
    bodovi = student[2]
    
    if bodovi < 50:
        rjecnik_rangova["Nedovoljan"] += 1
    elif bodovi < 65:
        rjecnik_rangova["Dovoljan"] += 1
    elif bodovi < 80:
        rjecnik_rangova["Dobar"] += 1
    elif bodovi < 90:
        rjecnik_rangova["Vrlodobar"] += 1
    else:
        rjecnik_rangova["Izvrstan"] += 1

print(studenti)
print(rjecnik_rangova)
