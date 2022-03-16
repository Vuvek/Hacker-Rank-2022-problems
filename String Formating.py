
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





