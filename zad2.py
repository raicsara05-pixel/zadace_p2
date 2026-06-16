'''
Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
'''

import random

imena = [
    "Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", 
    "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", 
    "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", 
    "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", 
    "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan", 
    "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip", 
    "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", 
    "Matej", "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", 
    "Magdalena", "Marko", "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", 
    "Petar", "Emanuel", "Helena", "Antonio", "Petar"
]

rjecnik_imena = {}
for ime in imena:
    if ime in rjecnik_imena:
        rjecnik_imena[ime] += 1
    else:
        rjecnik_imena[ime] = 1

studenti_ocjene = {}
brojac = 1
for ime in imena:
    jedinstveno_ime = f"{ime}_{brojac}"
    studenti_ocjene[jedinstveno_ime] = random.randint(1, 5)
    brojac += 1

rjecnik_ocjena = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for ocjena in studenti_ocjene.values():
    rjecnik_ocjena[ocjena] += 1

prosli = 0
for ocjena in studenti_ocjene.values():
    if ocjena > 1:
        prosli += 1

ukupno = len(studenti_ocjene)
postotak_prolaznosti = (prosli / ukupno) * 100

print(rjecnik_imena)
print(rjecnik_ocjena)
print(postotak_prolaznosti) 
