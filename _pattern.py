# #1 1 1
# #2 2 2
# #3 3 3

# for i in range(1,4): #outer loop => rows
#     for j in range(1,4): #inner loop => cols
#         print(i,end="   ")
#     print()

# # A A A A A 
# # B B B B B 
# # C C C C C 
# # D D D D D 
# # E E E E E 
# n=int(input("Enter numbers of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ") #chr builtin to convert char into ASCII
#     print()

# # *
# # * *
# # * * *
# n=int(input("Enter numbers of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end=" ")
#     print()

# # A B C
# # A B
# # A 
# n=int(input("Enter numbers of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

# #     * 
# #    * * 
# #   * * * 
# #  * * * * 
# # * * * * * 
# import time
# n=int(input("Enter numbers of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(1)
#         print("*",end=" ")
#     print()