# import random
# print(random.randint(1,11))
import random
# def ball():
#     ball_c = random.randint(1,10)
#     return ball_c

# def bat():
#     runs = 0
#     while True:
#         user_hit = int(input("Enter your hit: "))
#         if user_hit in range(1,11):
#             ball_c = random.randint(1,10)
#             if user_hit == ball_c:
#                 print(f"I also choose {user_hit} Out")
#                 print(runs)
#                 break
#             else:
#                 print(f"I chose {ball_c}")
#                 runs+=user_hit
#         else:
#             print("Odd even is only for numbers in range 1-10...Try again!")   
#             continue
# a=bat()

with open("manual.txt" ,"r") as m:
        content = m.read()
        print(content)
        
