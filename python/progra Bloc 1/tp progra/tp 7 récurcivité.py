#ex1
def factorial(n):
    """Returns the factorial n!
    parameters
    ----------
    n:strictly positive integers(int)

    returns
    -------
    f:factorial of n(int)
    """
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(10))

print("-----------------------------------------------------------------")

#ex number of letters in a word

def longueur(mot):
    s = 0
    if mot =='':
        return 0
    else:
        return 1 +longueur(mot[1:])

print(longueur("salut"))

print("-------------------------------------------------------------------")

#ex 2
def max_min_in_list(list):
    if list == []:
        return float('-inf'), float('inf'), 0, 0
    else:
        nbr = int(list[0])
        max, min, min_number, max_number = max_min_in_list(list[1:])
        if nbr > max:
            max = nbr
            max_number = 1
        elif nbr < min:
            min = nbr
            min_number = 1
        elif nbr == max:
            max_number += 1
        elif nbr == min:
            min_number +=1
        return max,min,max_number,min_number
print(max_min_in_list([4,7,8,6,54,7,7,2,45,88]))

    
    




#ex 3
def palindrome(mots):
    if len(mots) <=1:
        print("it's a palindrome")
    elif mots[0] != mots[-1]:
        print("it's not a palindrome")
    else:
        return palindrome(mots[1:-1])
    
print("-------------------------------------------------------")
    
#ex 4

def number_of_vowels(word):
    []
    if word == "":
        return 0
    else:
        word