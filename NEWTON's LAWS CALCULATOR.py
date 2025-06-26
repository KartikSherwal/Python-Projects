print("Hello,User please tell me your so that we can know you better!")
name = input("Tell us your name: ")
print(f"Hello {name} I am Rycoon your Bot made by NANOBEING!")
#print(f"Hello, {name} nice to meet you welcome Newton's laws of motion")
print("Tell us what do you want.Type find in front of your value that you want to ask! and 'quit' to exit.")
F = input("FORCE(F): ")
M = input("MASS(M): ")
A = input("ACCELARATION(A): ")
try:
    while True:
        if F == 'find':
             ma = float(M) * float(A)
             print(f"{ma} N.")
             break

##        if F == 'quit':
##             print("Thanks for using us!")
##             break
    
        if M == 'find':
             fa = float(F) / float(A)
             print(f"{fa} kg.")
             break

##        if M == 'quit':
##             print("Thanks for using us!")
##             break

        if A == 'find':
             fm = float(F) / float(M)
             print(f"{fm} m/s^2")
             break

        if A == 'quit' or F == 'quit' or M == 'quit':
             print("Thanks for choosing us!")
             break
except Exception:
    print(f"{name} I think you have given an invalid input check you responses again by opening the program again!!")
print(f"Thank you {name} for choosing us felt nice to help you!")
print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")
