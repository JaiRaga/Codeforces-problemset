def foxAndSnake(n, m):
    s = ''
    back = True
    done = False

    for i in range(1, n + 1):
        if i % 2 != 0:
            for j in range(1, m + 1):
                s += '#'
            s += '\n'
        elif i % 2 == 0:
            for j in range(1, m + 1):
                if back and not done:
                    if j == m:
                        s += '#'
                        back = not back
                        done = True
                        continue
                elif not back and not done:
                    if j == 1:
                        s += '#'
                        back = not back
                        done = True
                        continue

                if ((back or done) and j != m) or ((not back or done)
                                                   and j != 1):
                    s += '.'
            s += '\n'
            done = False

    return s


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    print(foxAndSnake(n, m))