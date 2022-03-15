def extractg1(x):
    if x[1] > 1:
        return x
def extract1(x):
    if x[1] == 1:
        return x

s = "aabbbccde"
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

dic = sorted(d.items(),key = lambda x:x[0])
dg1 = list(filter(extractg1,dic))
d1 = list(filter(extract1,dic))
d = sorted(dg1 , key=lambda x : x[1],reverse=True)
print(d,d1,dic)
counter = 0
for key,value in d:
    if counter < 3:
        print(key,value)
        counter += 1
    else:
        break


for key,value in d1:
    if counter < 3:
        print(key,value)
        counter += 1
    else:
        break
