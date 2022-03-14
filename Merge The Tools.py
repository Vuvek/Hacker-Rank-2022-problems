# Link:-  https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=false

def merge_the_tools(string, k):
    l = len(string)//k
    j = 0
    m = k
    for i in range(l):
        s = ""
        
        u = string[j:m]
        if k != 1:
            j = j + k
            m = m + j
        else:
            j = j + k
            m = j + 1
        for n in u:
            if n not in s:
                s += n
        print(s)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k