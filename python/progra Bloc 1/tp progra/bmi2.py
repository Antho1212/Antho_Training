sexe = str(input("men or women?"))
weight = float(input('give your weight :'))
height = float(input('give your height :'))
bmi = weight/height **2
if sexe == "men" :
    pi = ((height*100)-100)-((height*100)-150)/4
elif sexe == "women" :
    pi = ((height*100)-100)-((height*100)-120)/4
else:
    pi = "fuck you"

print("your bmi",bmi)
if  bmi <25 :
    print("your good captain")
elif bmi< 18.5:
    print("youre a fucking skeleton go eat")
elif bmi < 30:
    print("go gym bro")
elif bmi < 35:
    print("your fat as fuck")
elif bmi < 40:
    print("wtf are you lying? youre dead xd, how do you leave your bed xd, and how do you past the door ?")
elif bmi:
    print("hello big mom")   
else:
    print("you don't exist on my fucking algo xd")

print("your ideal weight",pi)
if weight < pi :
    print("you need to eat more for the prime")
elif weight > pi :
    print("you should to go gym for the prime")

batminton_time = (weight - pi)*9000/330 
basketball_time = (weight - pi)*9000/390 
boxing_time = (weight - pi)*9000/770
if weight > pi :
    print("you need to lose ",weight - pi)
    print("time of batminton",batminton_time,"basketball",basketball_time,"boxing",boxing_time)
    




















