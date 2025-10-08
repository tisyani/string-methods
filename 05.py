"""
Feladat: Kérj be egy email címet a regisztrációhoz, majd ellenőrizd, hogy Gmail-es-e.
"""

gmail = input("give me your email address: ")


if gmail.endswith("@gmail.com"):
    print ("its a gmail")
else :
    print ("not gmail")