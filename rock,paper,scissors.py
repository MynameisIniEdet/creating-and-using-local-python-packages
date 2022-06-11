#this is a rock, paper, scissors game



import random
def rps_game():
    print("Rock , Paper , Scissors\n R for Rock, P for Paper, S for Scissors")
    print("START")
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')

    print("Rock, Paper, Scissors")
    user=input("Enter R,P or S")
    user=user.upper()
    print("\n")
    CPU=str(random.randint(1,3))
    CPU_moves={'1':'R','2':'P','3':'S'}
    CPU=CPU_moves[CPU]

    for i in user:
        if((user=='R' and CPU=='S')  or(user=='P' and CPU=='R') or (user=='S' and CPU=='P')):
            print(f"CPU: {CPU}")
            print(f"Player: {user}")
            print("\n YOU WIN!!!")
        
        elif(user==CPU):
            print(f"CPU: {CPU}")
            print(f"Player: {user}")
            print("\n DRAW!")
            print(restart())

        else:
            print(f"CPU: {CPU}")
            print(f"Player: {user}")
            print("\nYOULOSE!!!\n Please try again")
            print(restart())

def restart():
    user_input=input("Would you like to play again? Type Yes or No \n\n")

    if user_input.lower()=="no":
        return False
    elif user_input.lower()=="yes":
        return True

def startgame():
    while True:
        user_input=input("READY TO PLAY!!\n ROCK,PAPER,SCISSORS!!\n R for Rock, P for Paper, S for Scissors\n Type 'go' to start playing")
        print ("\n")
        if user_input=="go":
            print(rps_game())
            if not restart():
                return


startgame()