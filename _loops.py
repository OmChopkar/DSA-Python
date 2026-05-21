# for i in range(5): #default i=0 -> 0  1   2   3   4
#     print(i)

# for i in range(2,11): #starting, ending
#     print(i)

# for i in range(2,11,2): #starting, ending, steps
#     print(i) 

# #Table 2-10 / 11-20
# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
# print()
# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)

# #Table 2-10 / 11-20
# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
# print()
# for i in range(11,21):
#     print(i*1," ",i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

# for i in range(1,5):
#     if i == 3:
#         break 
#     print(i) # 1 2 

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i) # 1 2 4 5



# #OUTPUT
# #1   5
# #2   4
# #4   2
# #5   1

# #zip() is used to take multiple range function
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i,"   ",j)


# #-While Loop-
# #Initialization
# #while(condition):
# #   stmt
# #   inc/dec

# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("Not in Budget")
#         continue
#     print(item)
# else:
#     print("You have purchased everything")



# #When username password matches -> successful, else -> enter again
# #username="admin"
# #password="admin"

# while True:
#     username=input("Enter Username:")
#     password=input("Enter Password:")
#     if username=="admin" and password=="admin":
#         print("Login Successful...")
#         break
#     else:
#         print("Enter Again...")
#         print()