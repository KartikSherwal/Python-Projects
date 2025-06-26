from time import sleep
name = input("Enter your Name: ").title()
print(f"\n\t Hello, {name} I am Rycoon! Your bot Assistance!")
print("\n\tGive me a number and I will tell you whether it is prime or composite!")
while True:
    try:
        num = int(input("\n\tEnter the number: "))
        count = 0
        for number in range(1,num+1):
            if num%number==0:
                count+=1
        sleep(0.5)
        print("\n\n")
        if count> 2:
            print(f"\t\tI think {num} is a Composite number.")
            
        if count== 2:
            print(f"\t\tI think {num} is a Prime number.")
            
        if count<2: 
            print(f"\t\tI think {num} is neither composite nor prime!")
            
        
    except Exception:
        print("Please enter a number only! ")
        continue

    print("\n")
    chance = input("Do you want some more (y for yes/ n for no): ")
    if chance == 'y' or chance == 'Y' or chance == 'yes':
        continue
    if chance == 'n' or chance == 'N' or chance == 'no':
        break
    else:
        break
print(f"\n\tThank you very much {name} for choosing us! Always there for your help!")
print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")
