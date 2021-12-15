from collections import Counter

# Read input file
with open('input') as f:
    lines = f.readlines()

# Make the rules dictionary we're going to use
rulesDict = dict()
rulesList = lines[2:]
for rule in rulesList:  # Dissapointed in myself, FUCK
    rule = rule.strip()
    key, value = rule.split("->")
    key, value = key.strip(), value.strip()
    rulesDict[key] = value
# Key   = the two letters
# Value = the letter we put between the two letters

# Function to do one step into the given list and
# returns the "stepped in" list
def step(lista):
    returnList = list()
    for i in range(len(lista) - 1):
        returnList.append(lista[i])
        # if this is optimized, maybe the second part has a chance
        for key in rulesDict.keys(): 
            if (lista[i] + lista[i + 1] == key):
                returnList.append(rulesDict[key])
                break # Time optimization XD
    returnList.append(lista[-1])  # Yeah, cringe
    return returnList

# Making the steps, should be a easier way
myList = list(lines[0].strip())
step1 = step(myList)
step2 = step(step1)
step3 = step(step2)
step4 = step(step3)
step5 = step(step4)
step6 = step(step5)
step7 = step(step6)
step8 = step(step7)
step9 = step(step8)
step10 = step(step9)

# Using counter from collections
counts = Counter(step10)

# Getting the min and max keys
maxLetter = max(counts, key=counts.get)
minLetter = min(counts, key=counts.get)
# Idk why plain max, min doesnt work, whatever
print("Max counts has", maxLetter, "with", counts[maxLetter])
print("Min counts has", minLetter, "with", counts[minLetter])

# Printing the result
print("Result", counts[maxLetter] - counts[minLetter])


# Can't possibly do the second part, too big of a time complexity
myStep = step(myList)
for i in range(39):
    myStep = step(myStep)
    
counts = Counter(myStep)
# Getting the min and max keys
maxLetter = max(counts, key=counts.get)
minLetter = min(counts, key=counts.get)
# Idk why plain max, min doesnt work, whatever
print("Max counts has", maxLetter, "with", counts[maxLetter])
print("Min counts has", minLetter, "with", counts[minLetter])

# Printing the result
print("Result", counts[maxLetter] - counts[minLetter])
