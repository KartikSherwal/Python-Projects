from time import sleep
name = input("What is your Name: ")
print("Hello {} I am your Bot Assistant Rycoon!".format(name.title()))
print("Enter the number and I will give you it's table till 10")

while True:
    try:
        num = int(input("\nEnter the number: "))
        print(f"\nHere we go with your table of {num}")
        for n in range(1,11):
            sleep(0.3)
            print(f"{num} x {n} = {num*n}")
        print(f"\n\tThank you very much {name.title()} for choosing us! Always there for your help!")
        break
    except Exception:
          print(f"{name.title()} you had entered an invalid input please try again")
          
print("\t\t\t\t\tDeveloper: KARTIK SHERWAL \n\t\t\t\t\tAlliance: NANOBEING")
