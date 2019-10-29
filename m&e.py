def evenOrOdd(n):
    if n == 1:
        return 'Ehab'
    elif n % 2 == 0:
        return "Mahmoud"
    else:
        return "Ehab"
            






if __name__ == "__main__":
    n = int(input().strip())
    print(evenOrOdd(n))