import random
import math
guessnum = math.floor(random.random()*1000)
chance = 10
while(chance):
    value = int(input("你还有"+str(chance) + "次机会,[请输入数字1-1000]:"))
    print(value)
    if(value>guessnum):
        print("太大了")
    elif(value <guessnum):
        print("太小了")
    else:
        print("正确")
        break
    chance = chance -1

# value = float(input(str(index+1) + "/5请输入成绩:"))