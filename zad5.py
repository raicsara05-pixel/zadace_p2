'''
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata ime.prezimeX@sum.ba 
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.

Istražiti greedy i non-greedy quantifiers.
'''

import re

email_regex = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
eduid_regex = r"^[a-zA-Z]+\.[a-zA-Z]+[0-9]*@sum\.ba$"

user_email = input("Unesite e-mail: ")
if re.match(email_regex, user_email):
    print("E-mail je validan.")
else:
    print("E-mail nije validan.")

user_eduid = input("Unesite eduID: ")
if re.match(eduid_regex, user_eduid):
    print("eduID je validan.")
else:
    print("eduID nije validan.")
