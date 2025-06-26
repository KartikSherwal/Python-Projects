from time import sleep
name = input("Enter your Name: ")
print(f"Hello {name.title()} my name is Rycoon, I am the Bot of Nanobeing.")
sleep(1.0)
print("Please enter a word/number and I will Count letters in it!")
sleep(0.5)

while True:
    
    try:
        
        print("\tEnter Q to quit anytime")
        word = input("Enter the content: ")
        if word == "q" or word == "Q":
            break
        print(f"\n{word} has {len(word)} words (including the space that you have given)")
        sleep(0.8)
    except Exception:
        print("\n\nPlease enter a word Only!")
        
print(f"\n\tThank you very much {name.title()} for choosing us! Always there for your help!")
print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")
