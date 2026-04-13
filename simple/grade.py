m=int(input("Enter mark :"))
print("Invalid input\n") if m<0 or m>100 else print("Grade : A\n") if m>=90 else print("Grade : B\n") if m>=75 else print("Grade : C\n") if m>=60 else print("Grade : D\n")
