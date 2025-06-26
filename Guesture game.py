print("Hello I am Rycoon The Bot of Nanobeing!")
print("Let us play a game i will think of a number and you have to guess it!")
name = input("What is your name: ")
print(f"Hello {name} let's play the game!")
import random
comp = random.randint(1,100)
ask = None
guesses = 0
while (ask != comp):
    try:
        ask = input("Please enter a number: ")
        if ask == 'quit' or ask == 'exit':
           break
        user = int(ask)
        if user == comp:
             print("You guessed it right!")
             guesses += 1
             print(f"You guessed it in {guesses} guesses!")
             break
        else:
             if (user <= comp):
                 print("You Guessed it wrong.Enter a larger number!")
                 guesses += 1
             else:
                 print("You Guessed it wrong.Enter a smaller number!")
                 guesses += 1
    except ValueError:
        print("Please enter a number only!")
    
##file = 'Record.txt'
##with open(file) as f:
##    content = int(f.read())
##if(guesses<content):
##    print("You have just broken the challenged score!")
##    with open(file, 'w') as f:
##            f.write(str(guesses))


