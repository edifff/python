def fnumber(num_list, number):
    l = len(num_list)-1
    f=0
    while l-f >1:
        m =  ((l + f) // 2)
        if num_list[m] == number:
            return number
        elif num_list[m] < number:
            f = m
        else:
            l = m
    if abs(number-num_list[f]) == abs(number-num_list[l]):
        return num_list[f]
    elif abs(number-num_list[f]) < abs(number-num_list[l]):
        return num_list[f]
    else:
        return num_list[l]
s = list(map(int, input().split(' ')))
a=list(map(int, input().split(' ')))
b=list(map(int, input().split(' ')))
for i in range(s[1]):
    print(fnumber(a, b[i]))