
# By First Method
'''

def print_formatted(number):
    for i in range(1,number+1):
        d = str(i).rjust(len(bin(number)[2:]),' ')
        o = oct(i)[2:].rjust(len(bin(number)[2:]),' ')
        h = (hex(i)[2:].rjust(len(bin(number)[2:]),' ')).upper()
        b = bin(i)[2:].rjust(len(bin(number)[2:]),' ')
        print("{} {} {} {}".format(d,o,h,b))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

'''






# def print_formatted(n):
#     for i in range(1,n+1):
#         # hexadecimal_result = format(i,"01X")
#         s = str(bin(n)[2:])
#         l=len(s)
#         print(f"{i:>{l}} {oct(i)[2:]:>{l}} {hex(i)[2:].upper():>{l}} {bin(i)[2:]:>{l}} ")

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


from re import L


def merge_the_tools(string, k):
    l = len(string)//k
    j = 0
    m = k
    for i in range(l):
        s = ""
        
        u = string[j:m]
        j = j + k
        m = m + j
        for n in u:
            if n not in s:
                s += n
        print(s)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)