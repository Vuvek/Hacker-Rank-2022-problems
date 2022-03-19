A = list(map(int,input().split()))
k = int(input())

t = []
c = 1
for i in A[0:-1]:
    
    for j in range(c,len(A)):
        t.append((i,A[j]))
    c+=1

s = list(map(sum,t))
s = list(filter(lambda x:x<k,s))
if len(s) == 0:
    print('-1')
else:
    print(max(s))