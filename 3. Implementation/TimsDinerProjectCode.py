#Keeping track of how many of each menu item has been ordered.
import datetime
import time

from counter import *


z=datetime.datetime.now()

continueOrder='Y'
countAdd=0

orderVal=[]
countList={1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:0}
#List storing values of amount of each item ordered.

if z.strftime("%H")>= '10' and z.strftime("%H")<= '18':
    z=datetime.datetime.now()
    print(z)

    from menuItems import *
    

#Allowing menu items to be called from a list (and assign each item a price).
  
    menuNum={0:'Placeholder', 1:'All day(large)',2:'All day(small)',3:'Hot dog',4:'Burger',5:'Cheese Burger',6:'Chicken Goujons',7:'Fries',8:'Salad', 
          9:'Milkshake',10:'Soft Drinks',11:'Still Water',12:'Sparkling Water'}

    price={'Placeholder':0, 'All day(large)':5.50, 'All day(small)':3.50, 'Hot dog':3.00, 'Burger':4.00, 'Cheese Burger':4.25, 'Chicken Goujons':3.50, 'Fries':1.75,
           'Salad':2.20, 'Milkshake':2.20, 'Soft Drinks':1.30, 'Still Water':0.90, 'Sparkling Water':0.90}

    tableNum=0

    orderList=[]

    while continueOrder == 'Y':
        while tableNum < 1 or tableNum > 10:
            tableNum=int(input("What is your table number?"))  #Keeping track of which table number the order is from
            if tableNum < 1 or tableNum > 10:
                print("Value out of range.")
            else:
                break

        orderLen=int(input("Input the number of items you will order."))

        total=0
        totalOrderVal=0


        for i in range (0,orderLen):
            order=int(input("Input the number for the menu item you will order(1-12)"))
            
            if order<1 or order>12:
                      print("Value is out of range")
                      break
            x=menuNum.get(order)
            orderList.append(x)
            currentPrice=0
            for n in range(0,orderLen-1):
                if x=='All day(large)':
                    countList[1]=countList[1]+1
                    print("All day(large) :", countList[1])
                elif x=='All day(small)':
                    countList[2]=countList[2]+1
                    print("All day(small) :", countList[2])
                elif x=='Hot dog':
                    countList[3]=countList[3]+1
                    print("Hot Dog :", countList[3])
                elif x=='Burger':
                    countList[4]=countList[4]+1
                    print("Burger :", countList[4])
                elif x=='Cheese Burger':
                    countList[5]=countList[5]+1
                    print("Cheese Burger :", countList[5])
                elif x=='Chicken Goujons':
                    countList[6]=countList[6]+1
                    print("Chicken Goujons :", countList[6])
                elif x=='Fries':
                    countList[7]=countList[7]+1
                    print("Fries :", countList[7])
                elif x=='Salad':
                    countList[7]=countList[7]+1
                    print("Salad :", countList[7])
                elif x=='Milkshake':
                    countList[8]=countList[8]+1
                    print("Milkshake :", countList[8])
                elif x=='Soft Drinks':
                    countList[9]=countList[9]+1
                    print("Soft Drinks :", countList[9])
                elif x=='Still Water':
                    countList[10]=countList[10]+1
                    print("Still Water :", countList[10])
                elif x=='Sparkling Water':
                    countList[11]=countList[11]+1
                    print("Sparkling Water :", countList[11])

            #Assigning each item a price

            y=price.get(x)
            print(x, y)
            currentPrice=y
            print(currentPrice)
            total=total+currentPrice
        orderVal.append(total)


        print("Here are the ordered items and the total price for Table", tableNum, ".")
        print(orderList)            

        print(total)

        #Keeping a running total of order values

        totalItemCounter=input("Would you like to see the amounts of each item ordered(Y/N)?")

        if totalItemCounter=='Y':
            for l in range(len(countList)):
                print(countList[l+1])
        elif totalItemCounter=='N':
            print("Ok.")
        else:
            print("Incorrect input")

        totalOrder=input("Would you like to see the totals of all orders so far?(Y/N)")
        if totalOrder=='Y':
            print(orderVal)
        elif totalOrder=='N':
            print("Ok.")
        else:
            print("Incorrect input")

        continueOrder=input("Do you want to order again?(Y/N)")
        if continueOrder == 'N':
            break
        break
else:
    print("Sorry, but the shop is closed.")
    print("Come between 10 AM and 6PM")
    time.sleep(5)
print("Please come again! :D")
