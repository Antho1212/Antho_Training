#tp machine 1
#ex1
print('Hello world')
#ex1.2
print('hello \nworld')
#ex2
print(3+4)
#ex3
x = 4
y = 2
print(x + y)
#ex4
age = 18
print('I am ',age,' years old')
#ex5
price = 100
discount = 0.2
reduction_amount = price*discount
final_price = price - reduction_amount
print('the price is ',price,' the discout is ',discount*100,' pourcent and the final price is ',final_price)
#ex6
food = 250
logement = 500
university = 850
price = (food*12*5) + (logement*12*5) + (university*5)
print(price)
#ex7
from random import*
print(randint(1,100))
#ex8
print((randint(1,100)) + (randint(1,100)))
#ex9.1
a = 42
b = a / 2
a = a + 1
c = a + 1
d = a + b + c
print( a, b, c, d)
#9.2
a = 2
b = 3
a = 2 * a
a = a + b
c = a + b
a = 2
d = a + b
print( a, b, c, d)