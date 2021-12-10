with open('input') as f:
    lines = f.readlines()

prev = 0
count = 0
for line in lines:
    now = int(line)
    if (now > prev):
        count += 1
        print(now, "(increased)")
    print(now, "(decreased)")
    prev = now
    
print("Count:", count - 1) # subtract one because of the first measurment