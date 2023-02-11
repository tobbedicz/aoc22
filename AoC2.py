f = open("input2.txt", "r")
scorevar =['A', 'B', 'C']
winvar = ['X', 'Y', 'Z']
winmatrix = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]
winmatrix2 = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]
sum = 0
for line in f:
    firstpos = scorevar.index(line[0])
    secondpos = winvar.index(line[2])
    sum +=winmatrix2[firstpos][secondpos] #Uppgift 2
    #sum +=winmatrix[firstpos][secondpos] #Uppgift 1
print(sum)
f.close()