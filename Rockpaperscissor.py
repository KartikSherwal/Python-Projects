from time import sleep
ask = input("What is your name: ")
name = ask.title()
intro = "Let's play rock paper scissor"
print(f" Hello, {name} nice to meet you! I am Rycoon the bot assistant from NANOBEING made for you!")
print(intro)
user_score = 0
rycoon_score = 0
matches = 0
import random
# Main loop begins 🎃🎃
while True:
    try:
        

        user_action  = input("\n \tEnter a choice (rock,paper,scissor):")
        user_possible_actions = ['rock' ,'paper','scissor']
        possible_actions = ['rock', 'paper', 'scissor']
        computer_action = random.choice(possible_actions)
        print(f"\nYou chooses {user_action} and I chooses {computer_action}.")
        if user_action not in user_possible_actions:
            print(f"\n{name} {user_action} is not a valid input!")
            print("Make sure to write the correct spelling and NOT TO WRITE ANY LETTER IN CAPITALIZED FORMAT!")
     
    

        elif user_action == computer_action:
            print(f"\nBoth players selected {user_action}. It's a tie!")
          
        elif user_action == 'rock':
            if computer_action == 'scissor':
               print("\nRock destroys scissor. You win!")
               user_score += 1

            else:
                 print("\nPaper covers rock. You lose!")
                 rycoon_score += 1
               
        elif user_action == 'paper':
            if computer_action == 'scissor':
                 print("\nScissor cuts paper. You lose!")
                 rycoon_score += 1
                 
            else:
                 print("\nPaper covers rock. You win!")
                 user_score += 1
                
        elif user_action == 'scissor':
            if computer_action == 'rock':
                print("\nRock smashes scissor.You lose!")
                rycoon_score += 1
            elif computer_action == 'paper':
                   print("\nScissor cuts paper.You win!")
                   user_score += 1
        matches += 1
                
        play_again = input("Do you want to play again(y/n): ")
        if play_again.lower() == 'y':
             continue

        if play_again.lower() == 'n':
            print(f"\tYour score :- {user_score}")
            print(f"\tMy score :- {rycoon_score}")

            if rycoon_score > user_score:
                print("Yeah! Rycoon wins! You also played nice!")
                
            elif rycoon_score == user_score:
                print("It's a tie! You played nice!")

            else:
                print(f"Congats {name} You won! You are a pro player!")
            print(f"You have played {matches} matches with me! It was interesting!")
            print(f"\nThank you very much for playing with me {name},I enjoyed a lot with you and hope you so!")
            print("\nWe will meet again! I,Rycoon will miss you.B'bye!!")
            break
                
        elif play_again != 'y' or 'n':
              print("You gave an invalid input for playing again! I think there is a problem try again!")
              continue
    except Exception:
      print("Invalid input!")

print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")    
sleep(120)    
