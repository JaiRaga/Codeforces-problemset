if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n, m = map(int, input().strip().split())
        lis = list(map(int, input().strip().split()))
        s = sum(lis)
        if len(lis) == 1:
            print(lis[0])
        elif s >= m:
            print(m)
        else:
            print(s)
