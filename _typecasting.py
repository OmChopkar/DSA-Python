# #Type Casting : Conversion of one datatype to another
# #input() accepts everything as a String

# print("2"+"2")
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# print("Sum:",a+b)

#----------------------------------------------------
# #int() used to convert
# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))
# #print(int(10+5j)) #Error - complex value cant be convert into integer
# #print(int("3.14")) #Error - Floting value String cant be convert into integer
# #print(int("Om")) #Error - String to Integer not possible

#----------------------------------------------------
# #float() used to convert
# print(float(3.14))
# print(float(True))
# print(float(False))
# print(float("4"))
# #print(int(10+5j)) #Error - complex value cant be convert
# #print(int("3.14")) #Error - Floting value String cant be convert
# #print(int("Om")) #Error - String cant be convert

#----------------------------------------------------
# #complex() is used to convert -> Except String all possible conversion
# print(complex(3))
# print(complex(3.14))
# print(complex(True))
# print(complex("4"))
# print(complex(5,-3))
# print(complex(True,False))
# print(complex("Om")) #Error - String value cant be converted

#----------------------------------------------------
# #bool() is used to convert
# print(bool(0)) #False
# print(bool(1)) #True
# print(bool(0.0)) #False
# print(bool(1.0)) #true
# print(bool(3.14))
# print(bool(1+0j)) #True
# print(bool(0+0j)) #False
# print(bool(-1)) 
# print(bool(True))
# print(bool(False))
# print(bool(""))
# print(bool("Om"))