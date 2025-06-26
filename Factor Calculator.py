from time import sleep
Name = input("Enter your name: ")
name = Name.title()
print(f"Hello {name} I am Rycoon your Bot Assistant!")
sleep(0.7)
print("\nGive me a number and I will tell you its Factors")
sleep(0.5)
while True:
    try:
        num = int(input("Enter the Number: "))
        
        print("Calculating.....")
        sleep(0.5)
        print(f"Here are the Factors of {num}: ")
        count = 0
        for i in range(1,num+1):
            if num%i == 0 :
                sleep(0.2)
                count+=1
                print(i)
        sleep(0.7)
        print(f"{num} has {count} factors")
        #print(count)
        sleep(1.0)
        if count>2:
            print(f"Also {num} is a Composite no!")
        elif count == 2:
            print(f"Also {num} is a Prime no!")
        elif count == 1:
            print(f"Also {num} is neither Prime nor Composite!")
        sleep(0.3)    
        print(f"\t\t\tThanks for choosing us {name} ! Always there for your help!")
        
        break
        
    except Exception:
        print(f"{name} you have given an Invalid Input Please try again!")
        continue

print("\n\t\t\t Developer: KARTIK SHERWAL \n\t\t\tAlliance: Nanobeing")





##        for n in range(2,num):
##            if num%i == 0:
##                print( "Also" ,num, "is a Composite number.")
##                break
##            elif num == 0 or 1:
##                print(num, "is neither Prime nor Composite.")
##            else:
##                print("Also" ,num, "is a Prime number.")
        
##        a = str(i)
##        if len(a) == 2:
##            print(f" Also {num} is a Prime number.")
##        elif num == 1:
##            print('1 is neither Prime nor Composite')
##        else:
##            print(f" Also {num} is a Composite number.")
                
        
    

