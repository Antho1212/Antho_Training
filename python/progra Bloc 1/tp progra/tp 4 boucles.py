#ex1
years = 10
while years > 0:
    print ("c'est dans %d ans je m'en irai j'entends le loup le renard chanter" %years )
    years -= 1

print("---------------------------------------------------------------------")

#ex2
a = 0
b = 10
while a < b or b>0 :
        print(a)
        a += 1
        if b % 2 != 0:
            print(b)
        b -= 1

print("------------------------------------------------------------------------")


#ex3
for i in range(1,15,3):
     print(i)

print("-------------------------------------------------------------------------")


#ex4
x = 525
total = 0
div = 0
if x > 0:
     for i in range(1,x+1):
          if x % i == 0:
               total += 1
               div = i
               print("diviseur:",div)
     print("total :",total)        
    
else :
     print("no negative number")

print("---------------------------------------------------------------------------")

#ex5
y = int(input("please enter a interger an a positive number: "))
while y < 0:
     y = int(input("please enter a interger an a positive number: "))
total = 0
div = 0
for i in range(1,y+1):
     if y % i == 0:
          total += 1
          div = i
          print("diviseur:",div)
print("total :",total)   
if total == 2:
     print(y,"it's a prime number")      

print("----------------------------------------------------------------------------")

#ex6 matheo code
def average_temperature(numbers_list: list[int]):
    """Calcule la moyenne des nombres donné

    Parameters
    ----------
    numbers_list : liste des températures donnée par le joueur (list[int])

    Returns
    -------
    Result: la moyenne des nombres entré
    """
    total_number = 0

    for number in numbers_list:
        total_number += number

    return total_number / len(numbers_list)


temperature_list = []

while True:

    player_input = input("Enter a Temperature: ")
    try:
        input_number = int(player_input)

        if input_number == -100:
            print("Stopped adding temperatures.")
            break

        else:
            temperature_list.append(input_number)
            print("Value added.")

    except:
        print("Invalid input")

average = average_temperature(temperature_list)
amount_temp = len(temperature_list)

print(f"The {amount_temp} last day's average temperature was: {average}")


#ex 6 my code
def averag_temperature():
     number = 0
     total = 0
     t = float(input("enter a temperature: "))
     
     print("temperature add")
     while t != -100:
          total += t
          number += 1
          t = float(input("enter a temperature: "))
          print("temperature add")
     average_t = total/number 
     print("the average temperature is ",average_t)
     return average_t

averag_temperature()

print("---------------------------------------------------------")

