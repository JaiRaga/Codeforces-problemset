def game(s):
    if s.count('A') > s.count('D'):
        return 'Anton'
    elif s.count('A') == s.count('D'):
        return 'Friendship'
    return 'Danik'

if __name__ == "__main__":
    n = input().strip()
    st = list(map(str, input().strip()))
    s = [i for i in st]
    print(game(s))