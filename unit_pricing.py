"""Calculates total amount from quantity and price"""
q = input("Please enter the Quantity desired: ")
p = input("Please enter the Unit price: $")
t = int(p) * int(q)
print("The Quantity desired is: " + q)
print("The Unit Price is      : $" + p)
print("The Total Amount is    : $" + str(t))
