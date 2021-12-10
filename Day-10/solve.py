with open('input') as f:
    lines = f.readlines()

open_list = ["[", "{", "(", "<"]
close_list = ["]", "}", ")", ">"]
score = 0
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
'''
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
'''
  
# Function get score of parentheses with a stack
def get_score(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return scores[i]
    if len(stack) == 0:
        return 0
    else:
        return 0
        # print("what")
    

for line in lines:
    score += get_score(line)

print(score)