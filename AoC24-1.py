f = open("input1 2024.txt", "r")
sum = 0
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in f: #for each row in file
    row = str(line)
    minindex = []
    maxindex = []
    min= 0
    max = 0
    for c in range(len(numbers)): #for each entry in numbers matrix
        min = row.find(numbers[c])
        max = row.find(numbers[c])
        for i in range(len(row)): #for each character in row
            k = row.find(numbers[c], i)
            if k!= -1:
                if k > max:
                    max = k
        minindex.append(min)
        maxindex.append(max)
    min = 1000
    max = -1000
    minpos = 0
    maxpos = 0
    for j in range(len(minindex)):
        if (minindex[j] > -1 and minindex[j] < min):
            min = minindex[j]
            minpos = j
        if (maxindex[j] > -1 and maxindex[j] > max):
            max = maxindex[j]
            maxpos = j
    min = 10*(1 + (minpos % 9))
    max = (1 + (maxpos % 9))
    print(line)
    print(minindex)
    print(maxindex)
    print(min)
    print(max)
    sum+= min + max        
print(sum)
f.close()