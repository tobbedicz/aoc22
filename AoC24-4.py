f = open("input4 2024.txt", "r")
totpoints = 0
nbcards = [1] #uppgift 2
cardindex = 0 #uppgift 2
for line in f: #for every row: build array with winning numbers, then go through each number to that
    strlinetemp = str(line)
    strline = strlinetemp[8:len(strlinetemp)] #remove the "Card   X:" part
    winningnumbers = strline[0: strline.find('|') + 1]
    print(winningnumbers)
    c = 0
    n = 0
    while c < (len(strline) - len(winningnumbers)): #count the number of winning numbers n
        print(strline[len(winningnumbers) + c: len(winningnumbers) + c+3])
        if winningnumbers.find(strline[len(winningnumbers) + c: len(winningnumbers) + c+3]) > 0: 
            if n < 1:
                n+=1
            else:
                #n = n * 2 #uppgift 1
                n+=1 #uppgift 2
        c+=3
    #totpoints+=n #uppgift 1
    #uppgift 2:
    print(n) #number of winning numbers => number of consecutive scratchcards to give copies of
    print(nbcards[cardindex]) #number of scratchcards on this row
    if (n == 0 and len(nbcards) < cardindex + 2):
        nbcards.append(1)
    for i in range (0, n):
        if len(nbcards) < cardindex + i + 2:
            nbcards.append(nbcards[cardindex] + 1)
        else:
            nbcards[cardindex + i + 1]+=nbcards[cardindex]
    totpoints+=(nbcards[cardindex])
    cardindex+=1
print(nbcards)               
print(totpoints)
f.close()