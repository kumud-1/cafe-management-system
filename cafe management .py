menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffe':80,
}
#greeting
print("WELCOME TO OUR CAFE")
print("PIZZA:Rs40\nPASTA:Rs50\nBURGER:Rs60\nSALAD:Rs70\nCOFFE:Rs80")

order_total=0

item=input("Enter the name of item you want to order=")
if item in menu:
    order_total += menu[item]
    print(f"your item {item}has been added to your order")
else:
    print(f"ordered item {item}is not available yet!")

another_order=input("Do you want to add another item?(yes/no)")
if another_order=="yes":
    item_2=input("enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2}has been added to order ")
    else:
        print("ordered item{item_2}is not avaiable!")
    print(f"the total amount of items to pay is {order_total}")