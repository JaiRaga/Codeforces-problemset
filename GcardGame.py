def cardGame(arr1, arr2):
    table = []
    hand = []

    for i in arr1:
        for j in i:
            table.append(j)
    
    for i in arr2:
        if i[0:1] == table[0] or i[1] == table[1]:
            return 'YES'
    return 'NO'


if __name__ == "__main__":
    arr1 = [input().strip()]
    arr2 = list(map(str, input().strip().split()))
    print(cardGame(arr1, arr2))