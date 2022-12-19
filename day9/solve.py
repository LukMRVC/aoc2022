import sys

# class Node:
#     def __init__(self, id: str)

directions = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    direction, step = line.split(' ')
    directions.append((direction, int(step)))
    

visited = set()

head_position = (0, 0)
tail_position = (0, 0)

def add(f, s):
    return f[0] + s[0], f[1] + s[1]


dir_step = {
    'D': (-1, 0),
    'U': (1, 0),
    'R': (0, 1),
    'L': (0, -1),
}


for direction, step in directions:
    for s in range(step):
        visited.add(tail_position)
        head_position = add(head_position, dir_step[direction])
        # print('H', head_position)
        
        dx = abs(head_position[1] - tail_position[1])
        dy = abs(head_position[0] - tail_position[0])
        
        if dy > 1 or dx > 1:
            if tail_position[0] != head_position[0] and tail_position[1] != head_position[1]:
                next_step = (1 if head_position[0] > tail_position[0] else -1, 1 if head_position[1] > tail_position[1] else -1)
                tail_position = add(tail_position, next_step)
            else:
                next_step = (0, 0)
                if tail_position[0] == head_position[0] and tail_position[1] != head_position[1]:
                    next_step = (0, 1 if head_position[1] > tail_position[1] else -1)
                elif tail_position[0] != head_position[0] and tail_position[1] == head_position[1]:
                    next_step = (1 if head_position[0] > tail_position[0] else -1, 0)
                tail_position = add(tail_position, next_step)
            
        # print('T', tail_position)
        
# print(head_position)

print(len(visited))

visited = set()
head_position = (0, 0)
knots = []
for _ in range(9):
    knots.append((0, 0))
    
for direction, step in directions:
    for s in range(step):
        # visited last knot
        visited.add(knots[8])
        head_position = add(head_position, dir_step[direction])
        # print('H', head_position)
        
        for idx, knot in enumerate(knots):
            # previous knot
            kp = head_position if idx == 0 else knots[idx - 1]
            kc = knot
            
            dx = abs(kp[1] - knots[idx][1])
            dy = abs(kp[0] - knots[idx][0])
            
            if dy > 1 or dx > 1:
                if knots[idx][0] != kp[0] and knots[idx][1] != kp[1]:
                    next_step = (1 if kp[0] > knots[idx][0] else -1, 1 if kp[1] > knots[idx][1] else -1)
                    knots[idx] = add(knots[idx], next_step)
                else:
                    next_step = (0, 0)
                    if knots[idx][0] == kp[0] and knots[idx][1] != kp[1]:
                        next_step = (0, 1 if kp[1] > knots[idx][1] else -1)
                    elif knots[idx][0] != kp[0] and knots[idx][1] == kp[1]:
                        next_step = (1 if kp[0] > knots[idx][0] else -1, 0)
                    knots[idx] = add(knots[idx], next_step)
            pass
        # print(knots)

print(len(visited))