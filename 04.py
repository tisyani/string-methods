"""
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma.
"""     

order = input("Give me your order: ")

replacement = order.replace("alma", "körte")

print (f"The order has been changed {replacement}")
