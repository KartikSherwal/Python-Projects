first_no = int(input("Enter the number: "))
sec_no = int(input("Enter the 2nd number: "))
minimum = min(first_no,sec_no)
for num in range(1,minimum+1):
     if((first_no%num == 0) and (sec_no%num == 0)):
                   print(num)
##                   print(max(num))

"""
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))
"""
