'''
Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.
'''

def sa_zada(s):
    if len(s) == 0:
        return s
    else:
        return sa_zada(s[1:]) + s[0]

# test funkcije
unos = input("Unesite string: ")
print("Rezultat:", sa_zada(unos))
