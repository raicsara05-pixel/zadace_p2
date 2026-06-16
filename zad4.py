'''
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, 
a završava kao prvo slovo prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
'''

import re

regex = r"^S(?=.*[0-5])(?=.* )[a-zA-Z0-9 ]*R$"

test_primjer = ["S3 R", "S tekst R", "S4R"]

for primjer in test_primjer:
    if re.match(regex, primjer):
        print("'" + primjer + "' -> Prolazi!")
    else:
        print("'" + primjer + "' -> NE prolazi.")
