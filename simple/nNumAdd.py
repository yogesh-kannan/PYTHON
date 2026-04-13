n=int(input("Enter a number : "))
sum=0;
if 1<=n<=100000:
   for i in range(1,n+1):
      sum+=i
   print("Addition of",n,"Numbers :",sum)
else:
   print("Invalid input")
