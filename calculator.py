def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b

while True: 
 print("Select Option:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Divsion\n5.Exit")
 choice=input("Choose Option(btw 1 to 5):")

 if choice=='5':
    print("Exit calculator")
    break
 if choice not in ['1','2','3','4']:
    print("Invalid Input!! Choose btw 1 to 5.")
    continue
 try:
   a=float(input("Enter the first no: "))
   b=float(input("Enter the second no: "))

   if choice=='1':
       print("Result:",add(a,b))
   elif choice=='2':
       print("Result:",sub(a,b))
   elif choice=='3':
        print("Result:",multi(a,b)) 
   elif choice=='4': 
       if b==0:
          print("Error: cannot divide by 0")
       else:  
          print("Result:",divide(a,b))

 except ValueError:
    print("wrong value!!\nPlease enter the valid numbers.")

 



     
