name = input("Enter your Name: ").title()
print(f"\n Hello {name} I am Rycoon The Bot of Nanobeing!")
print("\n")
print("Tell me a the numbers and I will be telling you the Lowest Common Multiple of the numbers.")
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    fnum1 = []
    fnum2 = []
    for i in range(1,num1+1): #Taking numbers from 1 to that number 🔢🔢
        if num1%i == 0:       # Checking the divisiblity to determine the factors ➗➗
            fnum1.append(i)   # Adding the factors in the predefined list fnum1   💤💤
    
         #Doing the same with second number 😇😇🤧
    for I in range(1,num2+1):
        if num2%I == 0:
            fnum2.append(I)
    for p in fnum1:
        if p in fnum2:
            hcf = p
    # print(hcf)
    lcm = int((num1*num2)/hcf) #Using the property num1*num2  = hcf*lcm 💖💗💖 #MAths zindabad 🤣🤣
    print("\n\t\tThe required lcm of the given numbers is " , lcm)
except Exception:
    print("Please enter a number only.") # AAgi baat samajh 😎😎

print(f"\n\tThank you very much {name} for choosing us! Always there for your help!")

print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")
