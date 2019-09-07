def easyProblem(arr):
    for i in arr:
        if i == 1:
            return "HARD"
    return "EASY"

if __name__ == "__main__":
    n = input().strip()
    arr = list(map(int, input().strip().split(' ')))
    print(easyProblem(arr))