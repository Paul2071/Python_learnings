import random

user_wins=0
computer_wins=0

print("Welcome to Rock Paper Scissors!")

options = ["r", "p", "s"]

while True:
    user_input = input ("Type in either R, P or S. Q to quit. ").lower()
    if user_input == "q":
        break

    #checks that input is correct (either r p or s)   
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick.upper() + ".")


    #user win conditions
    if user_input == "r" and computer_pick == "s":
        print("You won!")
        user_wins += 1
        
    elif user_input == "p" and computer_pick == "r":
        print("You won!")
        user_wins += 1
            
    elif user_input == "s" and computer_pick == "p":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("A draw!")    
        
    else: 
        print("Computer wins!")
        computer_wins += 1    
    

print("You won", user_wins, "times")
print("The computer won", computer_wins, "times")
print("Goodbye")