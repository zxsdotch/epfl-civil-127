WIDTH, HEIGHT = (5, 4)
grid = [0] * (WIDTH * HEIGHT)

def offset(x, y):
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        raise Exception("invalid offset", x, y)
    return x * HEIGHT + y

def get(x, y):
    return grid[offset(x, y)]

def set(x, y, v):
    grid[offset(x, y)] = v

def printGrid():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(get(x, y), end=" ")
        print()

set(4, 3, "A")
set(1, 2, "B")
printGrid()
