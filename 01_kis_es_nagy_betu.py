"""1️⃣ Kis- és nagybetűssé alakítás – névformázás
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),   
kisbetűs (pl. email összehasonlításhoz)
csak az első betű nagy (személyes üdvözlésnél).
"""

user = input("Please give me your username: ")

uppercase = user.capitalize()
print (uppercase)
lowercase = user.lower()
print (lowercase)
allcap = user.upper()
print (allcap)