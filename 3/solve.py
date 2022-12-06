import sys
import string

s = 0

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)

priorities = {p: i + 1 for i, p in enumerate(priorities)}

lines = []
# task 1
# for line in sys.stdin:
#     items = line.strip()
#     mid = len(items) // 2
#     first, second = set(items[:mid]), set(items[mid:])
#     bad_item = (first & second).pop()
#     s += priorities[bad_item]

# task 2
group = list() 
for line in sys.stdin:
    group.append(set(line.strip()))
    if len(group) == 3:
        badge = (group[0] & group[1] & group[2]).pop()
        s += priorities[badge]
        group.clear()
    
print(s)