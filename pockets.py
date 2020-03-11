if __name__ == "__main__":
    n = input().strip()
    coins = list(map(int, input().strip().split()))
    pockets = []
    for i in coins:
        pockets.append(coins.count(i))
    print(max(pockets))
