with open("input.txt","r") as f:
    contents = f.read()
    myDict = {}

    for word in contents.split():
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1


with open("output.txt", "w+") as g:
    for i in myDict:
        g.write("%s : %s \n" %(i,myDict[i]))