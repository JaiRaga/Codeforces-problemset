if __name__ == "__main__":
    n = int(input())
    lis = list(map(int, input().strip().split(' ')))
    s = lis.count(1)
    st = [0] * s
    i = 0

    # print(s, st)

    for x in range(len(lis)):
        if x == 0:
            st[i] += 1
            continue
        if lis[x] == 1:
            i += 1
            st[i] += 1
        else:
            st[i] += 1

        # print(s, st)

    print(s)
    for y in st:
        print(y, end=" ")
