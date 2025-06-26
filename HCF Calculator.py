first_no = int(input("Enter the number: "))
sec_no = int(input("Enter the 2nd number: "))
l1 = []
l2 = []

##maximum = max(first_no,sec_no)
# for num in range(1,min(first_no,sec_no)):
#     if first_no%num == 0:
#            if sec_no%num == 0:
#                    hcf= num
#                    print(hcf)
        
# print(hcf)
##                   print(max(num))

for num in range(1,first_no+1):
    if first_no%num == 0:
        l1.append(num)
for numm in range(1,sec_no+1):
    if sec_no%numm == 0:
        l2.append(numm)

for i in l1:
    if i in l2:
        hcf=i
print("Hcf of ",first_no," and ",sec_no, " is ", hcf)