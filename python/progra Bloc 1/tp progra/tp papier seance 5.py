def replace(mylist:list, begin:int, end: int, newlist: list):
    index_newlist = 0
    lenght = len(mylist)
    if begin > end:
        print("enter a correct number")
    elif end > lenght :
        print("end must be on the list")
    elif begin < 0:
        print("begin need to be postivive")
    for i in range (begin,end):
        mylist [i] = newlist[index_newlist]
        index_newlist += 1
    print(mylist)
replace([4,25,78],1,2,["salut"])
