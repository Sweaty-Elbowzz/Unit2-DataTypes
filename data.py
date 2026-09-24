# x = 3
# y = float(3)
# print(x,y)
# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i)
#     print(values[0])
# print(values[6])

# day_of_week = input("what day is it? ")
# if day_of_week == "Friday":
#     print("correct")
# else:
#     print("incorrect")

# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')

# x = "Jason"
# y= x.split("s")
# z = y[0]
# print(y)
# print(z)

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")


# sentence = "How much was the bill?"
# print(sentence)
# bill = float(input())
# sentence = "How was our service?"
# print(sentence)
# service_options = ("bad", "okay", "good", "great")
# print(service_options)
# service = input()
# if service == "bad":
#     print("Would you like to leave a 0% tip?")
# elif service == "okay":
#     print("Would you like to leave a 10% tip?") 
# elif service == "good":
#     print("Would you like to leave a 15% tip?")
# elif service == "great":
#     print("Would you like to leave a 20% tip?")
# response = input()
# if response == "yes":
#     if service == "bad":
#         tip = bill * 0
#     elif service == "okay":
#         tip = bill * 0.10
#     elif service == "good":
#         tip = bill * 0.15
#     elif service == "great":
#         tip = bill * 0.20
#     total = bill + tip
#     print("Your total is: ", total)

# if response == "no":
#     print("Your total is: ", bill)

# input = int(input("Enter a number: "))
# if input <= 0:
#     print("Please enter a positive number.")
# else:
#     for n in range(1, input + 1):
#         if input % n == 0:
#             print(n)

argument = int(input("Type a number: "))
argument2 = int(input("Type another number: "))

for n in range(1, argument + 1):
    if argument % n == 0:
        print(n)
for i in range(1, argument2 + 1):
    if argument2 % i == 0:
        print(i)
if n  == i :
    print(n)