#tp machine 2
#ex1
#voir feuille car diagramme
#ex2
angle_1 = 45
angle_2 = 45
angle_3 = 90

if angle_1 + angle_2 + angle_3 ==180:#verif if its a triangle
    if angle_1 == angle_2 == angle_3:
        print("it's a equilateral triangle ")
    elif angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        if angle_1 == angle_2 or angle_1 == angle_3 or angle_2 == angle_3:
            print("it's a triangle rectangle,isocele")
        else:
            print("it's a traingle rectangle")
    elif angle_1 == angle_2 or angle_1 == angle_3 or angle_2 == angle_3:
        print("it's a triangle isocele")
    else:
        print("it's a scalene triangle")
else:
    print("it's not a triangle")
    
#ex3
note = 21
if 20 < note:
    print('Liar')
elif 18 <= note:
    print("clutch")
elif 16 <= note:
    print("great")
elif 14 <= note:
    print(' nice job')
elif 12 <= note:
    print('good')
elif 10 <= note:
    print('w is w')
else:
    print("fail")
#ex4
p_threshold = 2.3
v_threshold = 7.41
volume = 50
pression = 50
if volume > v_threshold:
    if pression > p_threshold:
        print('stop everything stop bro stop!')
    else:
        print("need to reduce the volume")
elif pression > p_threshold:
    print('need to augmente the volume')
else:
    print('all is good')
#ex5
height = 1.75
weight = 80
sexe = 'men'
#pour un homme
#pi = ((height * 100) - 100) - ((height * 100) - 150)/4
#pour une femme
#pi = ((height * 100) - 100) - ((height * 100) - 120)/4

if sexe == 'men':
    pi = ((height * 100) - 100) - ((height * 100) - 150)/4
else:
    pi = ((height * 100) - 100) - ((height * 100) - 120)/4
print(pi)
bmi = weight/(height)**2
print(bmi)
if bmi < 18.5:
    print('need to eat')
elif bmi <= 25:
    print('ok')
elif bmi <= 32:
    print('go gym')
else:
    print('hard big mom')

lose = weight - pi
print('you need to lose :',lose,' kilo')
batminton = (lose*9000)/330
basketball = (lose*9000)/390
boxing = (lose*9000)/770
print(batminton,'hour of batminton',basketball,'hour of basketball',boxing,'hour of boxing')
#ex6
q = 100
cvd = 2.16
cva = 2.35
r = 20 * cvd + 30 * cva
if q <=30:
    p = 0.5 * q * cvd
elif q <= 5000:
    p = q * cvd + q* cva
else:
    p = 0.9 * q * cvd + q * cva
f = r + p
print(f)
#ex7
prix = 10
if 50 <= prix:
    print('you win a poster')
    if 500 <= prix:
        print('you win 20 minute with the artist')
        if 5000 <= prix:
            print('you win a private concert with max 20 persone')
else:
    print('you win nothing, give more')
    
#ex7 bis    
amount = 5000
if amount >= 5000:
    print("Concert for up to 20 people.")
    print("30 minutes with the artist.")
    print("Dedicated poster.")
elif amount >= 500:
    print("30 minutes with the artist.")
    print("Dedicated poster.")
elif amount >= 50:
    print("Dedicated poster.")
else:
    print("No advantage for this amount.")