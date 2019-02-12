# 知识点  python的数据类型
# 1. number     e.g.    a = 12
# 2. string     e.g.    b = 'hello' or c = "python"
# 3. list       e.g.    c = [1,2,3,4]

# HomeWork 1
# x is a number below 1000, we know x+100 is a square number(e.g. 4 =2*2 9=3*3)
# x + 168 is also a square number, what's x is?

# hint 1   how to know x is s square number

# function square(num) can know if x is a square number
def square(num):
    for value in range(num):
        if(value*value == num):
            return True
        else:
            return False

# example 1
x = 100
print(square(x))     #   True
# example 2
y = 101
print(square(y))     #  False

# hint2
#  please use [for] loop
