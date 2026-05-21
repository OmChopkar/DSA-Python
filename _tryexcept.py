#Occurs in Runtime
#Allows multiple exception in single except
# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("Cant divide by Zero")
# except ValueError:
#     print("Enter only integer values")
# except:
#     print("XYZ")

# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)

# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("Cant divide by Zero")
# except ValueError:
#     print("Enter only integer values")
# #finally and else cannot be used together
# finally: 
#     print("Always Executable")
# # else: 
# #     print("Everything is OK")


#Logs of error in a file
# import logging
# logging.basicConfig(filename="newFile.txt", level=logging.DEBUG)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
#     logging.exception(msg)
# print("Logging level is set up. Check 'newFile.txt' for log details.")