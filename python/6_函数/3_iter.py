def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5 ))
print(fact(100))


# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(n,i):
#     if n == 1:
#         return i
#     return fact_iter(n-1, n *i)
#
#
