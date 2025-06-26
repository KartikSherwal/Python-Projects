from time import sleep
#🆔🆔
Name = input("Enter your Name: ")
name = Name.title()
print("Enter The time for starting the timer.")
print("\n\t\tMake sure to enter the seconds only!")
sleep(0.7)

#The main Loop for program Starts 👇👇
while True:
    try:
        #Asking for the time⏲🙂
        num = int(input("Please Enter the time: "))
        print(num)
        sleep(0.3)

        # Main base of the program🎇✨🎉
        for i in range(1,num+1):
            num -=1
            sleep(1.0)
            print(num)
        sleep(0.5)
        #⏰⏰
        print(f"Times Up {name}")

        #Asking to start again🔄
        again = input("Do you want to run it again(yes/no): ")
        if again == "yes" or again == "y" or again == "Yes":
            continue

        elif again == "no" or again == "n" or again == "No":
            break
        
        else:
            print(f"{again} is an Invalid Input.. There may be a problem Try again")
            break
    except Exception:
        print("Please Enter a time only (integer form).")

# After coming out of main loop💨
print(f"\n\tThank you very much {name} for choosing us! Always there for your help!")
#🎊🎡
print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")
