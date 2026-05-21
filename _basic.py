# #Why Python is Dyanmic?
# #No need to declare the type of a variable
# #The interpreter checks the dataype in runtime

# age=21
# name="Om"
# pi=3.14
# result=True
# print(type(age)) #Returns datatype class
# print(type(name))
# print(id(pi)) #Address
# print(id(result))

# #Why fundamental datatypes are immutable?
# #Same values -> Same Address (Gives reference)
# maths=50
# chem=50
# print(id(maths))
# print(id(chem))


# #Conversion of rs into diff notes
# amount=int(input("Amount: "))
# print("100 Notes: ",amount//100)
# print("50 Notes: ",(amount%100)//50)
# print("20 Notes: ",((amount%100)%50)//20)
# print("10 Notes: ",(((amount%100)%50)%20)//10)
# print("5 Notes: ",((((amount%100)%50)%20)%10)//5)
# print("2 Notes: ",(((((amount%100)%50)%20)%10)%5)//2)
# print("1 Notes: ",((((((amount%100)%50)%20)%10)%5)%2)//1)