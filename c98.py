def countTheWords():
    fileName=input("enter the file name")
    wordCount=0
    file=open(fileName,"r")
    for i in file :
        words=i.split()
        wordCount = wordCount+len(words)
    print(wordCount)


countTheWords()