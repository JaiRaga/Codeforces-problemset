if __name__ == "__main__":
    n = int(input().strip())
    sum = 0
    for i in range(n):
        name = input().strip()
        if name == "Tetrahedron":
            sum += 4
        elif name == "Cube":
            sum += 6
        elif name == "Octahedron":
            sum += 8
        elif name == "Dodecahedron":
            sum += 12
        elif name == "Icosahedron":
            sum += 20
    print(sum)
