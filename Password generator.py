from time import sleep
import random
name = input("Enter your Name: ").title()
print(f" Hello, {name} nice to meet you! I am Rycoon the bot assistant from NANOBEING made for you!")
print('I will generate a very strong password for you that no one can guess!')
sleep(1.0)
a = ['a', ' b', 'c','d','e','f','g','h','i','j','k','l','m','n']
A = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N']
num = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
sym = ['@','#','&','*','$','~','!']
ra = random.choice(a)
rA = random.choice(A)
rnum = random.choice(num)
rsym = random.choice(sym)
rsym2 = random.choice(sym)
password = rA+ra+rsym+rnum+rsym2+name[:3]
print("Here is your strongest password make sure to remember it or note it down somewhere.")
print(f"\n\n\t\t'{password}'")
sleep(5.0)
