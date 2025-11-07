print("-------------------------------------------------------------------------------------") 

mesure_angle1 = int(input("enter les mesure_angles1 :"))
mesure_angle2 = int(input("enter les mesure_angles2 :"))
mesure_angle3 = int(input("enter les mesure_angles3 :"))
if mesure_angle1 + mesure_angle2 + mesure_angle3 != 180:
    print("it's not a triangle")
elif mesure_angle1 and mesure_angle2 and mesure_angle3 == 60:
    print("it's a equilateral triangle")    
elif mesure_angle2 or mesure_angle1 or mesure_angle3 == 90:
    print("it's triangle rectangle")
elif mesure_angle1 and mesure_angle2 == 60 or mesure_angle1 and mesure_angle3 == 60 or mesure_angle2 and mesure_angle3 == 60:
    print("isocele triangle")
else :
    print("triangle scalene")



