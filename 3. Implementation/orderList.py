orderList=[]

tableNum=int(input("What is your table number?"))  #Keeping track of which table number the order is from
orderLen=int(input("Input the number of items you will order."))
for i in range (0,orderLen):
    order=int(input("Input the number for the menu item you will order(1-12)"))
    if order<1 or order>12:
              print("Value is out of range")
              break
    x=menuNum.get(order)
    orderList.append(x)
    

print(orderList)            
