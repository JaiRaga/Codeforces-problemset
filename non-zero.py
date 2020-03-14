if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        l = int(input().strip())
        lis = list(map(int, input().strip().split()))
        c = lis.count(0)
        for i in range(c):
            remInd = lis.index(0)
            lis[remInd] += 1
        # print(lis, c)
        sum = 0
        pr = 1
        for i in lis:
            sum += i
            pr *= i
        # print(sum, pr)
        if sum == 0 or pr == 0:
            c += 1

        print(c)
