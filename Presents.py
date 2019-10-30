if __name__ == "__main__":
    n = input().strip()
    arr = list(map(int, input().strip().split(' ')))
    lis = [0]*len(arr)
    for i in range(len(arr)):
        lis[arr[i]-1] = i + 1
    for i in lis:
        print(i, end=" ")