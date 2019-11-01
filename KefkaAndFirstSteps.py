def inc(lis):
    ini = lis[0]
    c = 1
    arr = []
    for i in range(len(lis)):
        if i == 0:
            pass
        elif lis[i] >= ini:
            c += 1
            ini = lis[i]
            # print(lis[i], ini, c)
        else:
            ini = lis[i]
            arr.append(c)
            c = 1
    arr.append(c)

    return max(arr)

if __name__ == "__main__":
    n = input().strip()
    lis = list(map(int, input().strip().split(' ')))
    print(inc(lis))