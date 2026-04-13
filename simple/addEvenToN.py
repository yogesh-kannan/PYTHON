n=int(input("Enter a number : "))
sum=0;
if 1<=n<=100000:
   for i in range(0,n+1,2):
      sum+=i
   print("Addition of Even numbers between 0 to",n," :",sum)
else:
   print("Invalid input")
