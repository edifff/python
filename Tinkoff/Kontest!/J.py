def calculate_cut(numbers_list):
    otbt = []
    for numbers in numbers_list:
        n, m = numbers
        VS = [sum(range(i, i + n * m, m)) for i in range(1, m + 1)]
        HS = [sum(range(i, i + m)) for i in range(1, n * m + 1, m)]

        otvet = float('inf')
        direction = ''
        cut = 0

        for h in range(len(HS)):
            prom = 0
            for s in range(len(HS)):
                if s < h:
                    prom += HS[s]
                else:
                    prom -= HS[s]

            if abs(prom) < otvet:
                otvet = abs(prom)
                direction = 'H'
                cut = h + 1

        for v in range(len(VS)):
            prom = 0
            for s in range(len(VS)):
                if s < v:
                    prom += VS[s]
                else:
                    prom -= VS[s]

            if abs(prom) <= otvet:
                otvet = abs(prom)
                direction = 'V'
                cut = v + 1

        otbt.append([direction, cut])

    return otbt

def main():
    t = int(input())
    numbers_list = []
    for _ in range(t):
        numbers = list(map(int, input().split()))
        numbers_list.append(numbers)
    otbt = calculate_cut(numbers_list)

    for result in otbt:
        print(result[0],result[1])

if __name__ == "__main__":
    main()