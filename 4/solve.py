import sys

first_sections = []
second_sections = []
for line in sys.stdin:
    line = line.strip()
    
    f, s = line.split(',')
    first_sections.append(f)
    second_sections.append(s)
    

def is_contained(r1, r2):
    s1, e1 = r1.split('-')
    s1, e1 = int(s1), int(e1)
    
    s2, e2 = r2.split('-')
    s2, e2 = int(s2), int(e2)
    
    return set(range(s1, e1 + 1)).issubset(set(range(s2, e2 + 1)))

def overlap(r1, r2):
    s1, e1 = r1.split('-')
    s1, e1 = int(s1), int(e1)
    
    s2, e2 = r2.split('-')
    s2, e2 = int(s2), int(e2)
    
    return len(set(range(s1, e1 + 1)) & set(range(s2, e2 + 1))) > 0

s = 0

# for i in range(len(first_sections)):
#     if is_contained(first_sections[i], second_sections[i]) or is_contained(second_sections[i], first_sections[i]):
#         s += 1
        
for i in range(len(first_sections)):
    if overlap(first_sections[i], second_sections[i]) or overlap(second_sections[i], first_sections[i]):
        s += 1
        
        
print(s)