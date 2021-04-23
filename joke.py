def joke(arr1, arr2, arr3):
    a = list(arr1)
    b = list(arr2)
    c = list(arr3)

    # print(a, b, c)

    for i in arr1:
        if (c.count(i) > 0):
            c.remove(i)
        else:
            return 'NO'

    for i in arr2:
        if (c.count(i) > 0):
            c.remove(i)
        else:
            return 'NO'

    if len(c) == 0:
        return 'YES'
    return 'NO'


if __name__ == "__main__":
    arr1 = input().strip()
    arr2 = input().strip()
    arr3 = input().strip()
    print(joke(arr1, arr2, arr3))