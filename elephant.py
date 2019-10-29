def elephant(n):
    lis = [5, 4, 3, 2, 1]
    steps = 0
    num = n
    for i in lis:
        if n >= i:
            steps += (n // i)
            n %= i
        elif lis.count(n) > 0:
            steps += 1
            n = 0
    
    return steps
        


if __name__ == "__main__":
    n = int(input().strip())
    print(elephant(n))