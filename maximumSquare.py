if __name__ == "__main__":
    k = int(input().strip())
    for i in range(k):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        lis = []
        side = 0
        for i in range(n):
            lis.append(max(arr))
            arr.remove(max(arr))
            # print(lis, arr)
            if len(lis) > min(lis):
                break
            side = len(lis)
        print(side)
