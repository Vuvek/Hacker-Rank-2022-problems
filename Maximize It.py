# from itertools import product

# k,M = map(int,input().split())
# l = []
# for i in range(k):
#     l.append(list(map(int,input().split())))

# def fun(x):
#     p = 0
#     for i in x:
#         p = p + (i*i)
#     return p%M

# # print(*product(*l))
# print(max(*map(lambda x: sum(i*i for i in x)%M, product(*l))))


# l = [list(map(int, input().split()))[1:] for _ in range(k)]
# print(l)
# print(max(list(map(lambda x: sum(i*i for i in x)%M, product(*l)))))



from itertools import product


k,M = map(int,input().split())
l = []
for i in range(k):
    l.append(list(map(int,input().split()))[1:])
# l = (list(map(int, input().split()))[1:] for _ in range(k))
def fun(x):
    p = 0
    for i in x:
        p = p + (i*i)
    return p%M

print(*product(*l))
print(list(map(fun, product(*l))))
print(max(list(map(fun,product(*l)))))