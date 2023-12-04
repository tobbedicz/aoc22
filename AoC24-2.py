f = open("input2 2024.txt", "r")
colors = ["blue", "green", "red"]
target = [14, 13, 12]
id_count = 0
for line in f: #for every row in the file
    occurences = []
    for i in range(0, len(colors)): #for every color
        counter = 0
        start_index = 0
        for j in range(len(str(line))): #find every occurence of each color
            k = str(line).find(colors[i], start_index)
            if k!=-1:
                start_index = k + 1
                if int(str(line)[k-3:k-1]) > counter:
                    counter = int(str(line)[k-3:k-1])
                #if int(str(line)[k-3:k-1]) > target[i]:
                    #counter = 1
                    #counter+=int(str(line)[k-3:k-1])
        occurences.append(counter)
    print(line)
    print(occurences)
    id_count += occurences[0] * occurences[1] * occurences[2] 
    #if (occurences[0] == 0 and occurences[1] == 0 and occurences[2] == 0):
        #print("OK!")
        #id_str = str(line)[5: int(str(line).find(":"))]
        #print(id_str)
        #id_count +=int(id_str)
print(id_count)
f.close()