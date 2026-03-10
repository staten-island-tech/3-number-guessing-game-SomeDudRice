# x=10
# while x > 0:
#  print (x)
#  x = x - 1

# color = ""

# while color != "stop":
#     color = input("What is your favorite color? (type 'stop' to finish): ")
# print("glad to know your favorite color !")


isput = int(input("number"))
import random
my_list = []
answer = random.randint(1,10)
while not int(answer) == int(isput):
 print ('wrong')
 my_list.append(isput)
 isput = input("number")
print (answer,"is right")
print (my_list)

