b=float(input("Enter your Balance : "))
w=float(input("Enter amount to withdraw : "))
print("You can withdraw") if w>0 and w<=b and w%100==0 else print("You cannot withdraw")
