class MailChecker:
 def checker(self,s):
  n=s.count("@")
  if n!=1:
   print("INVALID")
  else:
   if s.endswith("@gmail.com")!=True:
      print("INVALID")
   else :
      f=0
      for i in range(0,s.index("@")-1):
         if s[i].islower()==True or s[i].isdigit()==True:
            f=0
         else:
            f=1
            break
      if f==0:
         print("VALID")
      else:
         print("INVALID")
a=MailChecker()
s=input("Enter a gmail:")
a.checker(s)
