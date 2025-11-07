import os
import pickle
values = ['camembert','coulomnier','brie']
file = open('cheeses.dat', 'wb')
pickle.dump(values, file)
file.close()
file = open('cheeses.dat','rb')
valuesToPrint = pickle.load(file)
file.close()
print(valuesToPrint)
# ex1 B
valuesToPrint.append('munster')
valuesToPrint.append('gryuere')
valuesToPrint = sorted(valuesToPrint)
file = open('cheeses.dat','wb')
pickle.dump(valuesToPrint, file)
file.close()
print(valuesToPrint)

print("-----------------------------------------------------------")

#ex2
#create the mountains.txt folders and write in
file = open('mountains.txt','w')
file.write('Arbizon ; 2831 ; Pyrenees\n')
file.write(';Arneto ; 3350 ; Pyrenes\n')
file.write(';Nanga Parbat ; 8125 ; Himalaya\n') 
file.write(';Broad Peak ; 8047 ; Karakoram \n')
file.write(';Gasherbrum I ; 8068 ; Karakoram\n') 
file.write(';1K2 ; 8611 ; Karakoram \n')
file.write(';Araille ; 2759 ; Pyrenees;\n')
file.write('Arnie ; 2504 ; Pyrenees ;\n')

def read_and_make_dico(file)->dict:
    data = {}
    file = open(file, 'r')
    lines = file.readlines()
    for line in file :
        line = lines.strip()
        line = line.split(' ; ')
        data[peak] = (hight,location)
    file.close()
    print(data)


print('-----------------------------------------------------------------------')

#ex3


print('------------------------------------------------------------------------')

#ex4
#make the strucuture
booksbyisbn = {{



}
}
booksbyauthors = {







}


