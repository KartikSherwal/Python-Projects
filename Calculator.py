print("Welcome to the calculator!")
ask = input("What is your name: ")
print(f" Hello,Nice to meet you {ask.upper()}! (type q to quit anytime!)")
while True:
    try:
        a = input("Tell us the no: ")
        if a == 'q':
           break
        z = int(a)
        b = input("Tell us the second number: ")
        if b == 'q':
           break
        y = int(b)
        print("Now tell us what do you want to do (m for multiply, s for subtraction, a for addition, d for division)")
        cal = input("Enter your operation: ")
        if cal == 'm':
           print(z*y)
        if cal == 's':
           print(z-y)
        if cal == 'a':
           print(z+y)
        if cal == 'd':
           print(z/y)
    except ValueError:
        print("Please enter a valid input!")
print("Thank you very much for choosing us!")
