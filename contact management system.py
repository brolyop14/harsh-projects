print("Welcome To Contact Management system" )
contacts={}
while True:
   print("\nOptions")
   print("1.Create Contact")
   print("2.Search Contacts")
   print("3.Update Contacts")
   print("4.Delete Contact")
   print("5.Count Contacts")
   print("6.View All Contacts")
   print("7.Exit")

   n=input("Choose The Option Btw 1 to 7: ")

   if n == '1':
      name=input("enter the name: ")
      if name in contacts:
         print(f"contact name {name} already exits!")
      else:
        age=input("enter the age: ")
        mobile_no=input("enter the no: ")
        contacts[name]={'age':int(age),'no':int(mobile_no)}
        print(f"contact name {name} successfully created!")

   elif n == '2': 
      name=input("enter the name: ")
      if name in contacts:
         contact=contacts[name]
         print(f"Name: {name}, Age: {contact['age']}, Mobile_No: {contact['no']}")

      else:
         print(f"Contact name {name} not found")  

   elif n == '3':
      name=input("enter the name to update contact: ")
      if name in contacts:
         name=input("enter the updated name: ")
         age=input("enter the updated age: ")
         mobile_no=input("enter the updated no: ")
         contacts[name]={'name':name,'age':int(age),'no':int(mobile_no)}
         print(f"contact name {name} successfully Updated!")
      else:
         print(f"Contact name {name} does not exit") 

   elif n == '4':
       name=input("enter the name to delete from contacts: ")
       if name in contacts:
          del contacts[name]
          print(f"contact name {name} successfully deleted!")
       else:
          print(f"Contact name {name} does not exit") 

   elif n == '5':
      print(f"The total no. of contacts is: {len(contacts)}") 
      
   elif n == '6':
         print("\nAll Contacts:")
         for name, info in contacts.items():
          print(f"Name: {name}, Age: {info['age']}, Mobile No: {info['no']}") 

   elif n == '7':
      print("closing the program!!")  
      break
   else:
      print("Invlid Input?")       
          
             

         
           
         
           
      
             
      
      



