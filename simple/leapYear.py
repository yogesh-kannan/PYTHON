y=int(input("Enter the year :"))
print("Leap year\n") if (y%4==0 and y%100!=0) or (y%4==0 and y%400==0) else print("Not a Leap year")
