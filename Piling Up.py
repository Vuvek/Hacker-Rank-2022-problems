# Link   -   https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=false

import math
n = int(input())

lis = []
for i in range(n):
    x = int(input())
    lis.append(list(map(int,input().split())))

for l in lis:

    l1 = []
    i = 0
    j = len(l)-1
    k = 1
    while k <= len(l):
        # print("hello")
        if l[i] >= l[j]:
            
            if len(l1)==0:
                
                l1.append(l[i])
                # print(l[i])
                # l1.append(l[j])
                i+=1
                # j-=1
                k+=1
            elif l1[-1]>=l[i]:
                l1.append(l[i])
                # l1.append(l[j])
                i+=1
                # j-=1
                k+=1
            else:
                print("No")
                # print(l1)
                break

        elif l[i] < l[j]:
            if len(l1)==0:
                l1.append(l[j])
                # l1.append(l[i])
                # i+=1
                j-=1
                k+=1
            elif l1[-1]>=l[j]:
                # print(l[i])
                l1.append(l[j])
                # l1.append(l[i])
                # i+=1
                j-=1
                k+=1
            else:
                print("No")
                # print(l1)
                break
    else:
        print("Yes")
        # print(l1)


        
