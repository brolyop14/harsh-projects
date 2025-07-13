import random

choices=["rock","paper","scissor"]

while True:
     user_choice=input("choose btw rock,paper,scissor or quit: ") 

     if user_choice == 'quit':
          print("thanks for playing!")
          break
     if user_choice not in choices:
          print("invalid input!!")
          continue
     
     computer_choice= random.choice(choices)
     print(f"computer choose: {computer_choice}")

     if user_choice == computer_choice:
          print("its a tie")

     elif(
          (user_choice == 'rock' and computer_choice == 'scissor') or
          (user_choice == 'paper' and computer_choice == 'rock') or
          (user_choice == 'scissor' and computer_choice == 'paper')       
            ):
          print("You Win!!!")   

     else:
          print("You Loss")




