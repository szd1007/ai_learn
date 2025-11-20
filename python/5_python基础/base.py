from ftplib import print_line

a = 100
if a > 100:
    print(a)
else:
    print(-a)


b = 1_0900
s = 'I\'m \"OK\"'

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(L[0][0])

print('\n')
age = 2
print('your age is', age)
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print('kid')


print('\n')


s = input('birth：')
birth = int(s)
if birth <2000:
    print('00前')
else:
    print('00后')


