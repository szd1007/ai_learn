# def power(x):
#     return x * x
#
# print(power(5))
# print(power(15))
from multiprocessing.pool import job_counter


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(' 5 p 3 is %d' %power(5, 3))

print (power(5))


def enroll(name, gender, age=6, city='Beijjing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah', 'F')

enroll('Bob', 'M', 7)

enroll('Adam', 'M', city='Tianjin')

def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

print(add_end())
print(add_end())

print()
print('_____')
print()
def add_end_none(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end_none())
print(add_end_none())
print(add_end_none())

def calc(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i*i
    return sum

print(calc([1, 2, 3]))
print(calc([1, 2, 3, 5, 7]))

def calcN(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print('calcN',calcN(1, 2, 3))

nums = [1, 2, 3]
print(calcN(*nums))

# 关键字参数
print("关键字参数")
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    if 'color' in kw:
        pass
    if 'job' in kw:
        print('has job', kw['job'])
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)

person('Bob', 36, city='Beijing')

person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

print('限制关键字参数名字，用*隔离')


def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')
# person('Jack', 24, city='Beijing')
person('Jack', 24, job='Engineer', city='Beijing')



print('测试')

def mul(*numbers):
    if len(numbers) == 0:
        raise TypeError
    sums = 1
    for n in numbers:
        sums = sums * n
    return sums


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')