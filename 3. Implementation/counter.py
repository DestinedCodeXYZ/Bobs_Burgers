orderList=[]

def totalItemCounter():
    totalItemCounter=input("Would you like to see the amounts of each item ordered(Y/N)?")

    if totalItemCounter=='Y':
        print(countList)
    elif totalItemCounter=='N':
        print("Ok.")
    else:
        print("Incorrect input")
