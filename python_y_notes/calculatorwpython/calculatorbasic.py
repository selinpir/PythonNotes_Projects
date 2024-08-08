print("---welcome to the calculator---")

print("1. addition (+) ")
print("2. subtraction (-)")
print("3. division (%)")
print("4. multiplication (*) ")

act=input(("please select an action (Press 'q' to exit):"))
if act=='q':
    print("leaving...")
    quit()

elif act=='1':
    num1=int(input("Please Enter the 1st number:"))
    num2=int(input("Please Enter the 2nd number:"))
    print("{}+{}={}" .format (num1,num2,num1+num2))

elif act=='2':
    num1=float(input("Please Enter the 1st number:"))
    num2=float(input("Please Enter the 2nd number:"))
    print("{}-{}={}" .format (num1,num2,num1-num2))

elif act=='3':
  try:
    num1=int(input("Please Enter the 1st number:"))
    num2=int(input("Please Enter the 2nd number:"))
    print("{} / {} = { :.2f} " .format(num1,num2,num1/num2))
  except ZeroDivisionError:
     print("You can't divide a number by 0! ")
  
elif act=='4':
    num1=float(input("Please Enter the 1st number:"))
    num2=float(input("Please Enter the 2nd number:"))
    print("{}x{}={}" .format (num1,num2,num1*num2))

else: 
   print("Invalid Option...")