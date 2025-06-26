print("Hello welcome to the Online LIBRARY! Enter 'q' to quit")
print("\nHello I am Rycoon the bot of NANOBEING I will help you find the book that you want!")
while True:
   
    name = input("What is your name: ")
    print(f"Hello {name} how can we help you!")
    if name == 'q':
        break
    book = input("Which book do you want: ")
    Class = input("Which class: ")
    List = ['Maths', 'Hindi', 'Civics', 'History', 'Science','Geography','geography','science','history','civics','hindi','maths','english']
    

    try:
        a = int(Class)
        
        if book not in List:
            print(f"No book named {book} is available for class {a}")
            break
           

        elif a >= 13:
            print(f"No book of {book} is available for class {Class}")
            break
        else:
            print(f"Book named {book} is available! for class {a}")
            break

    except ValueError:
        print("Please enter a valid input!")
        print("Make sure not to write very letter capitalize")
print("Thanks for choosing us!")

        
