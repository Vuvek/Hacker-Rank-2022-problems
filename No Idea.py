l = input(),input()

n = list(map(int,input().split()))

A = list(map(int,input().split()))

B = list(map(int,input().split()))

happiness = 0

for i in n:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)