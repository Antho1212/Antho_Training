weight = float(input("donne le poids\n"))
height = float(input("donne la taille\n"))
bmi = weight/height
print(bmi)
if bmi >17 and bmi < 25:
    print('bmi ok')
else:
    print('bmi a chier')