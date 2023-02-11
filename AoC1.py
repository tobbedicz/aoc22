f = open("input1.txt", "r")
sum = 0
maxsum = 0
uppgift = 2
sumlist = []
for line in f:
    #print(line)
    if line != "\n":
        sum += int(line)
    else:
        sumlist.append(sum)
        sum = 0
    if uppgift == 1:
        maxsum = max(maxsum, sum)
sumlist.sort(reverse = True)
print(sumlist)
print("Svaret är", maxsum)
print("Svaret på uppgift 2 är", sumlist[0] + sumlist[1] + sumlist[2])

f.close()