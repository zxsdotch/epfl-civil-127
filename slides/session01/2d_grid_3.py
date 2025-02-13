WIDTH, HEIGHT = (5, 4)
grid = [[0] * WIDTH for _ in range(HEIGHT)]

def get(x, y):
    return grid[y][x]

def set(x, y, v):
    grid[y][x] = v

def printGrid():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(get(x, y), end=" ")
        print()

set(4, 3, "A")
set(1, 2, "B")
printGrid()
