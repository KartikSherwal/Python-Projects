name = input("Enter your Name: ").title()
print(f" Hello, {name} nice to meet you! I am Rycoon the bot assistant from NANOBEING made for you!")
try:
    pro = int(input("Enter the product: "))
    su = int(input("Enter  the sum: "))
    di = int(input("Enter  the diff: "))
    l1 = []
    for i in range(1,pro+1):
        if pro%i == 0:
            l1.append(i)
            l1.reverse()
            for x in l1:
                if x*i == pro and x+i == su:
                    print(f"The numbers are {x} and {i}.")
                    print("Thanks for choosing us!")
                if x*i == pro and i-x == di:
                    print(f"The numbers are {x} and {i}.")
                    print("Thanks for choosing us!")
                    break
    print("(If you didn't got the output it meant that there are no such numbers.)")
except Exception as e:
    print("Please enter a number only...")
    

print(f"\n\tThank you very much {name} for choosing us! Always there for your help!")

print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")


