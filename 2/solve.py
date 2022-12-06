import sys

rock = 'A'
paper = 'B'
scissors = 'C'

def defeats(a, b):
    if a == rock and b == scissors:
        return True

    if a == scissors and b == paper:
        return True

    if a == paper and b == rock:
        return True
    
    return False

def wins(a):
    if a == rock:
        return scissors

    if a == scissors:
        return paper

    if a == paper:
        return rock
    
def loses(a):
    if a == rock:
        return paper

    if a == scissors:
        return rock

    if a == paper:
        return scissors
    
def id(a):
    return a
    
lines = [l.strip() for l in sys.stdin]

lines.pop()

score = 0

scores = {rock: 1, paper: 2, scissors: 3}

translator = {'X': rock, 'Y': paper, 'Z': scissors}

tie_score = 3
win_score = 6
lose_score = 0


mapper = {'X': wins, 'Y': id, 'Z': loses}


# for line in lines:
#     # win lose tie
#     wlt = 0
    
#     a, b = line.split(' ')
#     b = translator[b]
#     if defeats(b, a):
#         # win
#         score += win_score + scores[b]
#     elif a == b:
#         # tie
#         score += tie_score + scores[b]
#     else:
#         # loss
#         score += lose_score + scores[b]
        
for line in lines:
    # win lose tie
    wlt = 0
    
    a, b = line.split(' ')
    b = mapper[b](a)
    if defeats(b, a):
        # win
        score += win_score + scores[b]
    elif a == b:
        # tie
        score += tie_score + scores[b]
    else:
        # loss
        score += lose_score + scores[b]
    # print(score)

print(score)