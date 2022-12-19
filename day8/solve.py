import sys


grid = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    grid.append([int(h) for h in line])

# transposed grid
tgrid = [list(x) for x in zip(*grid)]

visible = len(grid[0]) * 2 # first and last row
visible += len(grid) * 2   # first and last column

visible -= 4 # corner points were added twice

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        l = grid[y][:x]
        r = grid[y][x + 1:]
        u = tgrid[x][:y]
        b = tgrid[x][y + 1:]
        
        if max(l) < grid[y][x] or \
            max(r) < grid[y][x] or \
            max(u) < grid[y][x] or \
            max(b) < grid[y][x]:
                visible += 1
        

print(visible)

scenic_scores = []
for _ in range(len(grid)):
    scenic_scores.append([0] * len(grid[0]))

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        qt = grid[y][x]
        
        l = 0
        for t in reversed(grid[y][:x]):
            l += 1
            if t >= qt:
                break
        r = 0
        for t in grid[y][x + 1:]:
            r += 1
            if t >= qt:
                break
        
        u = 0
        for t in reversed(tgrid[x][:y]):
            u += 1
            if t >= qt:
                break
            
        b = 0
        for t in tgrid[x][y + 1:]:
            b += 1
            if t >= qt:
                break
        
        scenic_scores[y][x] = l * r * u * b

max_scenic_score = 0
for scores in scenic_scores:
    max_scenic_score = max(max_scenic_score, max(scores))
    
print(max_scenic_score)