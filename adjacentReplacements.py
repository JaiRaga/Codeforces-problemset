if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] - 1

    for i in arr:
        print(i, end=" ")
