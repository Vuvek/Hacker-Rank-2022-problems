# from itertools import groupby
s = input()
# l = []
# for key,group in groupby(s,lambda x:x[0]):
#     print((len(list(group)),int(key)),end = " ")
    

l = []
coun = 1
for i in range(len(s)):
    if (i!= len(s)-1) and s[i] == s[i+1]:
        coun += 1
    else:
        print((coun,int(s[i])),end = " ")
        coun = 1
