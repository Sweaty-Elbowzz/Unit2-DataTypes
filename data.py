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

# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")


sentence = "How much was the bill?"
print(sentence)
bill = float(input())
sentence = "How was our service?"
print(sentence)
service_options = ("bad", "okay", "good", "great")
print(service_options)
service = input()
if service == "bad":
    print("Would you like to leave a 0% tip?")
elif service == "okay":
    print("Would you like to leave a 10% tip?") 
elif service == "good":
    print("Would you like to leave a 15% tip?")
elif service == "great":
    print("Would you like to leave a 20% tip?")
