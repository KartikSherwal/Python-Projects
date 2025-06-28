import random
name = input("Enter your name: ")
def tosswin(name):
    print(f"You won the toss {name} as you chose {user_num} and I chose {comp_num}")

def tosslost(name):
    print(f"I won the toss {name} as you chose {user_num} and I chose {comp_num}")

#User Bats
def user_bat_first():
    runs=0
    while True:
        hit = int(input("Enter your hit: "))
        ball_comp = random.randint(1,10)
        if hit in range(1,11):
            if hit != ball_comp:
                runs+= hit
                print(f"I bowled {ball_comp}.")
                print(f"Current score:{runs}")
            else:
                print("That's a wicket!")
                print(f"You played a inning of {runs}")
                break
        else:
            print("Please enter between 1-10 only..")
            continue 
    return runs    

#User Balls
def user_ball_first():
    runs = 0
    while True:
        ball_user = int(input("Enter your bowl (1 to 10 only): "))
        comp_hit = random.randint(1,10)
        if ball_user in range(1,11):
            if ball_user != comp_hit:
                runs+=comp_hit
                print(f"I hit a {comp_hit}.")
            else:
                print(f"Ohh no I Tried to hit {comp_hit} and OUT now!")
                print(f"I have made {runs} its your batting now!")    
                break
        else:
            print("Please enter a number in range 1-10...")
            continue
    return runs
#Comp Bats
# def comp_bat_first():
#     runs=0
#     while True:
#         comp_hit = random.randint(1,10)

'''User bats secondly'''
def user_bats_secondly(target):
    runs=0
    while True:
       comp_hit= random.randint(1,10)
       hit = int(input("Enter your hit: "))
       if hit in range(1,11):
            if runs==target and hit == comp_hit:
                print(f"I also choosed {comp_hit},Thus you are Out!")
                print("Its a tie!")
                break
            elif runs<target and hit == comp_hit:
                print(f"You lose by {target-runs} runs.")
                break
            else:
                runs+=hit
                print(f"Current score:{runs}")
                if runs>target:
                    print(f"You won by {runs-target} runs.")
                    break
       else:
           print("Please be in the range of 1-10")
           continue

def user_balls_secondly(target):
    runs = 0
    while True:
        ball_user = int(input("Enter your bowl (1 to 10 only): "))
        comp_hit = random.randint(1,10)
        if ball_user in range(1,11):
            if runs<target:
                if ball_user!= comp_hit:
                    runs+=comp_hit
                    print(f"I smashed a {comp_hit}. Current score:{runs}")
                else:
                    print(f"I tried to hit a {comp_hit} but am Out!")
                    print(f"You won by {target-runs} runs.")
                    break
            elif runs==target and comp_hit==ball_user:
                print(f" I scored exactly{runs} and OUT at this ball.")
                print("Therefore that`s a Tie!")
                break
            elif runs>target:
                print(f"You lose by {runs-target} runs.")
                break
            
        else:
            print("Please enter a number in range 1-10...")
            continue
            
        
# #Comp Balls
# def comp_ball():
#     pass

# If user won the toss.
def user_toss():
    while True:
        bat_ball= input("You will bowl or bat: ").lower().strip()
        if bat_ball not in ("bat","ball","bowl"):
            print(f"{bat_ball} is invalid choice Try again!")
            continue
        else:
            return bat_ball
def comp_toss():
    choice = ["bat","ball"]
    choosed = random.choice(choice)
    print(f"I will choose to {choosed} first.")
    return choosed


# COMPILATIONk

while True:
    toss = input("Enter your toss(in lowercase only): ")
    if toss not in ("e", "o","Even".lower(),"Odd".lower()):
       print(f"{toss} is an invalid choice please enter only odd or even.")
       continue
    else:
        user_num= int(input("Enter your num: "))
        comp_num = random.randint(1,10)
        total = user_num+comp_num
        
        if total %2==0 and toss=="e":
            tosswin(name)
            choice =user_toss()
            if choice =="bat":
                chase=user_bat_first()
                print(f"I have to make {chase+1} runs to win.")
                user_balls_secondly(chase+1)
                break
            else:
                userball = user_ball_first()
                print(f"You have to make {userball+1} runs to WIN!")    
                user_bats_secondly(userball+1)
                break

        elif total %2!=0 and toss=="o":
            tosswin(name)
            choice =user_toss()
            if choice =="bat":
                user_bat_first()
                chase=user_bat_first()
                print(f"I have to make {chase+1} runs to win.")
                user_balls_secondly(chase+1)
                break
            else:
                userball = user_ball_first()
                print(f"You have to make {userball+1} runs to WIN!")    
                user_bats_secondly(userball+1)
                break

        else:
            tosslost(name)
            comptoss=comp_toss()
            if comptoss == "bat":
              userball=user_ball_first()
              print(f"You have to make {userball+1} runs to WIN!")
              user_bats_secondly(userball+1)
              break
            else:
                chase=user_bat_first()
                print(f"Now I have a target of {chase+1}.")
                user_balls_secondly(chase)
                break
print("🎉 Game Over! Thanks for playing.")
