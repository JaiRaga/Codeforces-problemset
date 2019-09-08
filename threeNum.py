def threeNums(arr):
    num = []
    b = max(arr)
    arr.remove(b)
    for i in arr:
        num.append(b-i)
    for i in num:
        print(i, end=" ")

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    threeNums(arr)
