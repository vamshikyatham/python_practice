import random

def play():
    while True:
        player=input("What's your choice ?\n 'r' for rock \n 'p' for papaer \n 's' for scissor\n 'E' for exit form the Game\n Enter your choice:")
        computer=random.choice(['r','p','s'])
        if player==computer:
            print("It's a tie")
        elif (player=="r" and computer=="s") :
            print(f"You won! {player} --> {computer}")
        elif(player=="p" and computer=="r"):
            print("You won!  paper --> rock")
        elif(player=="s" and computer=="p"):
             print("You won!  scissor --> paper")
        elif(player=="E"):
            break
        else:
            print(f"computer won!  player:{player}-->computer:{computer}")
        
play()
        
