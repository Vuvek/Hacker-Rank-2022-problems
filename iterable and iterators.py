
from itertools import combinations
from math import comb

# n = int(input("Enter : "))
# l = list(input().split())
# k = int(input("Enter the index : "))
k = ['a','a','c','d']
combo = list(combinations(k,2))
counter = 0
for i in combo:
    if 'a' in i:
        counter += 1
print(combo)
print(counter)
prob = counter/len(combo)
print(prob)