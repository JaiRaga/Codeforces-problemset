def flight(s):
    letter = ''
    countF = 0
    countS = 0
    locations = [i for i in s]

    for i in range(len(locations)):
        if i == 0:
            letter = locations[i]
        elif locations[i] == 'F' and letter != locations[i]:
            countS += 1
            letter = locations[i]
        elif locations[i] == 'S' and letter != locations[i]:
            countF += 1
            letter = locations[i]

    if countS > countF:
        return 'YES'
    return 'NO'

if __name__ == "__main__":
    n = input().strip()
    s = list(map(str, input().strip()))
    print(flight(s))
            