import math
def my_move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-5))


def nop():
    pass


def quadratic(a, b, c):
    sAdd = -b + math.sqrt(b*b - 4*a*c)
    x = sAdd/(2*a)
    sSub = -b - math.sqrt(b*b - 4*a*c)
    y = sSub/(2*a)
    return x, y

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')






