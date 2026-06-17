print("welcome to my shop:")
print("the menu of the shop is: ")
menu={'milk':30,'eggs':50,'sugar':20}
total_bill=0
for item,price in menu.items():
    print(f"{item}:{price}")
    quantity=int(input(f"enter the quantity of the {item}: "))
    total_bill+=quantity*price
    print(f"the total bill is:{total_bill}")