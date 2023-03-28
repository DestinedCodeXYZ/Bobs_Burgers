printMenu=['1. All day(large)- £5.50', '2. All day(small)- £3.50', '3. Hot dog- £3.00', '4. Burger- £4.00', '5. Cheese Burger- £4.25', '6. Chicken Goujons- £3.50', '7. Fries- £1.75', '8. Salad- £2.20',
           '9. Milkshake- £2.20','10. Soft Drinks- £1.30','11. Still Water- £0.90','12. Sparkling Water- £0.90']

def menuItems():
    showMenu='Undefined'

    while showMenu!= 'Y' or showMenu!='N':
        showMenu=str(input("Would you like to see the menu(Y/N)?"))
        if showMenu=='Y':       #Validating input data
            showmenu='Y'
            for i in range(len(printMenu)):
                print(printMenu[i])
            break
        elif showMenu=='N':
            showMenu='N'
            print("Ok.")
            break
        else:
            print("Incorrect input")

menuItems()
