# x=10
# while x > 0:
#  print (x)
#  x = x - 1

# color = ""

# while color != "stop":
#     color = input("What is your favorite color? (type 'stop' to finish): ")
# print("glad to know your favorite color !")


righty_tighty = 0
import random
my_list = []
answer = random.randint(1,10)
isput = int(input("number"))
guessnum =0
while not righty_tighty == 1:
 if isput == answer:
  my_list.insert(guessnum, isput)
  righty_tighty ==  righty_tighty + 1
  break
 elif isput > answer:
  guessnum =+ 1
  my_list.insert(guessnum, isput)
  print ("too high")
  isput = int(input("number"))
 elif isput < answer:
  print ('too low')
  my_list.insert(guessnum, isput)
  guessnum =+ 1
  isput = int(input("number"))
 else:
  print("invalid")
  guessnum =+ 1
  my_list.insert(guessnum, isput)
  isput = int(input("number"))



print(isput, "is correct, here is your history",my_list)


# quart = 77
# plays =0
# m1 =4
# m2 = 9
# m3 = 3
# while quart > 0:   

#  if m1 < 35 and quart > 0:
#   quart -=1
#   plays = plays+1
#   m1+=1
#   if m1 == 35:
#    quart +=30
#    m1 =0

#  if m2 < 100 and quart > 0:
#   quart -=1
#   plays = plays+1
#   m2+=1
#   if m2 == 100:
#    quart +=60
#    m2 =0

#  if m3 < 10 and quart > 0:
#   quart -=1
#   plays = plays+1
#   m3+=1
#   if m3 == 10:
#    quart +=9
#    m3 =0
# print(plays)

# def casino (quart,spins,pyaouts,jackpots, ):
#     mturn=0
#     plays= 0
#     while quart > 0:
#      if jackpots[mturn] > spins[mturn]:
#       plays+=1
#       quart-=1
#       spins[mturn]+=1
#       if jackpots[mturn] == spins[mturn]:
#         quart+=pyaouts[mturn]
#      mturn+=1
#      if mturn ==2:
#       mturn ==0

# casino(77,[4,9,3],[30,60,9],[60, 100,10])

# print ('wrong')
# my_list.insert(isput)
# isput = input("number")
# print (answer,"is right")
# print (my_list)

