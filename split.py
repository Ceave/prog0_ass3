try:
    #Initialisierung
        #Libarys
    import sys

        #Load
    if len(sys.argv) == 1:
        data = open("input.txt")
    else:
        data = open(sys.argv[1])

        #Variables
    text = data.read()
    textLen=len(text)
    prevCount=0
    count = 151
    sms = ''
    data.close()

    #Work
    while True:
        try:
            if text[count] ==' ':
                count+=1
                #print("  found at position ",count,"!")
                sms += text[prevCount:count]
                sms+="("+str(abs(prevCount-count))+"/160)"
                sms+="\n------------------------------------------------------------\n"
                prevCount=count
                count=count+151
            count-=1
        except IndexError:
            sms+= text[prevCount:textLen]
            sms+="("+str(textLen-prevCount)+"/160)"
            sms+="\n------------------------------------------------------------"
            break

    print(sms)

    #Output
    if len(sys.argv) == 3:
        output = sys.argv[2]
    else:
        output = "output.txt"

    outFile = open(output,'w')
    outFile.write(sms)
    outFile.close()
except:
    print("error")
    sys.exit()
