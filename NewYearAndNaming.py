def newYear(nlis, mlis, num):
    if num < len(nlis) and num < len(mlis):
        return nlis[num - 1]+mlis[num - 1]
    return nlis[num % len(nlis) - 1] + mlis[num % len(mlis) - 1]


if __name__ == "__main__":
    n, m = map(int, input().strip().split(' '))
    nlis = list(input().strip().split(' '))
    mlis = list(input().strip().split(' '))
    q = int(input())
    for i in range(q):
        num = int(input().strip())
        print(newYear(nlis, mlis, num))
