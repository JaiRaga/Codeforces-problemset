def colonel(arr):
    high = max(arr)
    low = min(arr)
    highInd = arr.index(high)
    lowInd = None
    total = 0

    for i in range(len(arr)):
        if arr[i] == low:
            lowInd = i

    if (highInd < lowInd):
        total += highInd
        lowInd = len(arr) - lowInd - 1
        total += lowInd
        # print("111", total)
    else:
        total += highInd - 1
        lowInd = len(arr) - lowInd - 1
        total += lowInd
        # print("222", total)
    # print(high, low, highInd, lowInd)

    return total


if __name__ == "__main__":
    t = input().strip()
    arr = list(map(int, input().strip().split()))
    print(colonel(arr))