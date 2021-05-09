def sticks(lis):
    val = min(lis)
    if val % 2 == 0:
        return 'Malvika'
    return 'Akshat'


if __name__ == "__main__":
    lis = list(map(int, input().strip().split()))
    print(sticks(lis))