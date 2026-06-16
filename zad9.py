'''
Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
Jedna od funkcija neka bude definirana lambda izrazom, a druga standardnim načinom.
Zatim definiraj treću funkciju koja kao parametar prima naziv funkcije za ispis dobrodošlice i poziva je tako što pošalje vaše ime u nju.
Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije.
'''

def standardna_dobrodoslica(ime):
    return "Pozdrav " + ime + "!"

def lambda_dobrodoslica(ime):
    return "Dobrodošao " + ime + "!"

def izvrsi_dobrodoslicu(funkcija_za_ispis):
    moje_ime = "Sara"
    rezultat = funkcija_za_ispis(moje_ime)
    print(rezultat)

izvrsi_dobrodoslicu(standardna_dobrodoslica)
izvrsi_dobrodoslicu(lambda_dobrodoslica)
