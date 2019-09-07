def bears(a, b):
    for i in range(1, 100):
        a *= 3
        b *= 2
        if a > b:
            return i

if __name__ == "__main__":
    a,b = map(int, input().strip(). split(' '))
    print(bears(a,b))