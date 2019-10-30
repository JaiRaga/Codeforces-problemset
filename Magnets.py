def magnets(arr):
    count = 1
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(input().strip())
    # print(arr)
    print(magnets(arr))