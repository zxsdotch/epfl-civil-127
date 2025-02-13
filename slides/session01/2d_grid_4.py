WIDTH, HEIGHT = (5, 4)
grid = {}

def get(x, y):
    if (x, y) not in grid:
      return 0
    return grid[(x, y)]

def set(x, y, v):
    grid[(x, y)] = v

def printGrid():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(get(x, y), end=" ")
        print()

set(4, 3, "A")
set(1, 2, "B")
printGrid()
