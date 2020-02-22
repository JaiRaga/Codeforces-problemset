def grapes(x, y, z, a, b, c):
    Dimitry = 0
    michal = 0

    if a < x:
        return 'NO'
    if a >= x:
        a -= x
    if (a + b) >= y:
        Dimitry = (a + b) - y
    else:
        return 'NO'

    michal = Dimitry + c
    if michal >= z:
        return 'YES'
    return 'NO'


if __name__ == "__main__":
    x, y, z = map(int, input().strip().split(' '))
    a, b, c = map(int, input().strip().split(' '))
    print(grapes(x, y, z, a, b, c))
