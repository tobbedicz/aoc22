f = open("input8 2024.txt", "r")
count = -1
found = False
rows = []
rownums = []
instructions = ""
for line in f:
    if count == -1:
        instructions = str(line)
    elif count > 0:
        rows.append(str(line))
        rownums.append(str(line[0:3]))
    count+=1
currentinstr = "AAA"
count = 0
while found == False:
    for i in range(0, len(instructions) - 1):
        count+=1
        if instructions[i] == "L":
            currentinstr = rows[rownums.index(currentinstr)][7:10]
        elif instructions[i] == "R":
            currentinstr = rows[rownums.index(currentinstr)][12:15]
        if currentinstr == "ZZZ":
            found = True
            break
print(count)
f.close()
