def fnumber(num_list, number):
    l = len(num_list) - 1
    f=0
    while f <= l:
        m =  ((l - f) // 2)+f
        if num_list[m] == number:
            return "YES"
        elif num_list[m] < number:
            f = m + 1
        else:
            l = m - 1
    return 'NO'

s = list(map(int, input().split(' ')))
a=list(map(int, input().split(' ')))
b=list(map(int, input().split(' ')))
for i in range(s[1]):
    print(fnumber(a, b[i]))