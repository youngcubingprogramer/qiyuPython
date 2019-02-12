# 知识点  python的数据类型
# 1. number     e.g.    a = 12
# 2. string     e.g.    b = 'hello' or c = "python"
# 3. list       e.g.    c = [1,2,3,4]

# homework 2
# we want to write a lucky draw function

#  we want 3 kinds of prize:
# 1st prize   2nd prize  3rd prize

# 3 kinds of prize have different probability
# 1st prize   10%
# 2nd prize   30%
# 3rd prize   60%


# hint 1
# use list to save prize list
# prizes = ['1st','2nd','3rd']

# hint2
# different value print different string
# such as
# 0-10 print 1st
# 11-40 print 2nd
# 41-100 print 3rd

# hint3
# use function random.random() to get a random number
# eg
import random
print(int(random.random()*10))



# write a function called luckydraw()
def luckydarw():
    # finish by youself

# run luckydarw()
# output: 1st prize / 2nd prize / 3rd prize

# run 100times luckydarw()
# output:
    # 1st prize (10times)
    # 2nd prize (30times)
    # 3rd prize (60times)