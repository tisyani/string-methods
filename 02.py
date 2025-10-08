"""
Feladat: Kérj be egy üzenetet a felhasználótól, majd írd ki, hány karakterből áll. Hasznos lehet például Twitter/SMS hosszkorlátozás ellenőrzéséhez.
"""

message = input("Write something: ")

characters = len(message)
print(characters)   