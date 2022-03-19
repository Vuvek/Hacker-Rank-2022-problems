# Method 1

'''
s = input()
d = {}
for i in s:
    if i.isdigit() and int(i)%2 == 0:
        if 'even' in d:
            d['even'] = d['even']+[i]  
        else:
            d['even'] = [i]

    elif i.isdigit() and int(i)%2 != 0:
        if 'odd' in d:  
            d['odd'] = d['odd']+[i]
        else:
            d['odd'] = [i]

    elif i.isupper():
        if 'upper' in d:   
            d['upper'] = d['upper']+[i]
        else: 
            d['upper'] = [i]
         
    elif i.islower():
        if 'lower' in d:
            d['lower'] = d['lower']+ [i]
        else: 
            d['lower'] = [i]


try:
    l = d.get('lower')
    l.sort()
except:
    l=''
try:
    u = d.get('upper')
    u.sort()
except:
    u = ''
try:
    o = d.get('odd')
    o.sort()
except:
    o = ''
try:
    e = d.get('even')
    e.sort()
except:
    e = ''

print(''.join(l)+''.join(u)+''.join(o)+''.join(e))
'''

# Method 2

def fun_even(x):
    if int(x)%2 == 0:
        return x
def fun_odd(x):
    if int(x)%2 != 0:
        return x
        


import re

s = input()
s = ''.join(sorted(s))
print(s)
itr_lower = re.findall(r'[a-z]*',s)
itr_upper = re.findall(r'[A-Z]*',s)
itr_number = re.findall(r'[0-9]*',s)
# print(itr_lower,itr_number,itr_upper)
itr_upper = filter(lambda x:[i for i in x if i!=''],itr_upper)
# print(*itr_upper)
itr_lower = filter(lambda x:[i for i in x if i!=''],itr_lower)
# print(*itr_lower)
itr_even = filter(fun_even,itr_number[0])
even = "".join(list(itr_even))
itr_odd = filter(fun_odd,itr_number[0])
odd = "".join(list(itr_odd))

print(str(*itr_lower)+str(*itr_upper)+odd+even)


