'''
Napraviti generator funkcije za ispis svih parnih i 
svih neparnih brojeva manjih od prosljeđenog parametra.
'''

def parni_brojevi(n):
    lista = []
    for i in range(n):
        if i % 2 == 0:
            lista.append(i)
    return lista

def neparni_brojevi(n):
    lista = []
    for i in range(n):
        if i % 2 != 0:
            lista.append(i)
    return lista

# test funkcija
broj = int(input("Unesite broj: "))

print("Parni brojevi:", parni_brojevi(broj))
print("Neparni brojevi:", neparni_brojevi(broj))
