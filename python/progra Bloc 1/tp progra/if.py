print('availiable drinks: coke, juice, water, tea')
drink = input('what do you want to drink ?')

print('you ordered % drink)')
if drink == 'coke':
    print('price = 75 cts')
elif drink == "juice":
    print("price = 95 cts")
elif drink == 'water':
    print('price = 50 cts')
elif drink == "tea":
    print("price = 10 cts")
else:
    print("unhanaivailable drink")
