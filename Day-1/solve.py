with open('input') as f:
    lines = f.readlines()

def first(list):
    prev = 0
    count = 0
    for line in list:
        now = int(line)
        if (now > prev):
            count += 1
            # print(now, "(increased)")
        # print(now, "(decreased)")
        prev = now
    return count - 1 # subtract one because of the first measurment

def second(list):
    prevSum = 0
    count = 0
    for i in range(1, len(list)):
        if (i + 1 < len(list)):
            currSum = int(list[i-1]) + int(list[i]) + int(list[i+1])
        else:
            break
        
        if (currSum > prevSum):
            count += 1
            # print(currSum, "(increased)")
        # print(currSum, "(decreased)")
        prevSum = currSum
        
    return count - 1
        
# print("Count:", first(lines)) 
print("Count:", second(lines))