f = open("input3 2024.txt", "r")
schema = []
row = ""
for i in range(0, 142):
    row+='.'
schema.append(row)
for line in f:
    content = str(line)
    schema.append('.' + content[0:140] + '.')
schema.append(row)
# print(schema[1][1])
f.close()
sum = 0
for row in range(len(schema)): #for every row in the schema
    startcol = 0
    count = 0
    for column in range(len(schema[row])):
        if (schema[row][column]).isdigit():
            count+=1
        else:
            if count > 0:
                print(row)
                print(column)
                for i in range(0, 3):
                    for j in range(0, count+2):
                        if (schema[row + i - 1][column + j - count - 1].isdigit() or schema[row + i - 1][column + j - count - 1] == '.'):
                            print("Hej hej")
                        else:
                            print("Träff!")
                            #print(schema[row][column - count:column])
                            sum+=int(schema[row][column - count:column])
                            #print(schema[row][column - count:column-1])
                            #sum+=int(schema[row][column - count:column-1])
            count = 0
        
    print(sum)
    #print(row)
