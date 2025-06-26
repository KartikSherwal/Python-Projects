from time import sleep
name = input("Enter your Name: ").title()
print(f" Hello, {name} nice to meet you! I am Rycoon the bot assistant from NANOBEING made for you!")
# sleep(1.0)
print("\t\t\n\n  Please provide me some data to help you out....")
# sleep(2.0)
#print("\t\t\n\n The value you wants as answer put find or simply f... (Make sure that commands are case sensitive..)")
while True:
        try:
            ask = input("What do you want(Height(type h)/distance(type d)): ")
            if ask == 'q':
                break
            elif ask == 'd': 
                print("Type 0 instead of values to exit out of the programme....")
                # sleep(1.0)
                p = int(input("Enter the height: "))
                if p == 0:
                    break
                print("\t\t")

                print("\t\t\t\n\nI can cacluate only for angles equal to 30,45,60")
                sleep(1.5)
                print("\t\t\t")

                a = int(input("Enter the angle of elevation or depression(I can calculate only for angles = 30,45,60): "))
                if a==0:
                    break
                if a == 30:
                    b = 1.73*p
                elif a == 45:
                    b = p
                elif a == 60:
                    b = p*1.732/3
                else:
                    print(f"Sorry {name} but I can not calcuate for value of angles other than 30,45 and 60 😓😔")
                    break 
                
                print(f"\t\t\t\n\n\n\n Dear {name} the height for which you have asked about is {b} unit.")
                break
            
                print(f"\t\t\t\n\n\n Dear {name} the distance for which you had asked is {d} unit.")
                break
#Bhai Main kam to yha se start hua hai very critical bro....💪💆‍♂️💪🤘
            elif ask == 'h' :
                print("Type 0 instead of values to exit out of the programme....")
                sleep(1.0)
                b = int(input("Enter the distance of the object from your foot : "))
                sleep(1.0)
                if b==0:
                    break
                print("\t\t\t\n\nI can cacluate only for angles equal to 30,45,60")
                sleep(1.5)
                print("\t\t\t")
                a = int(input("Enter the angle of elevation or depression(I can calculate only for angles = 30,45,60): "))
                if a==0:
                    break

                if a == 30:
                    height = b*1.73/3
                elif a == 45:
                    height = b 
                elif a == 60:
                    height = b*1.73
                else:
                    print(f"Sorry {name} but I can not calcuate for value of angles other than 30,45 and 60 😓😔")
                    break
                print(f"\t\t\t\n\n\n\n Dear {name} the height for which you have asked about is {height} unit.")
                break
            else:
                print("I am still learning... till now I am only able to cacluate height and distance soon i would learn more regrading this topic 🤩🤗🤩.")
        except Exception:
            print("I think you have given a wrong value please provide us with the data again.")
            # print(Exception())  
print(f"\n\tThank you very much {name} for choosing us! Always there for your help!")

print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tCORPORATION👉👉: NANOBEING")               
            

            
  
