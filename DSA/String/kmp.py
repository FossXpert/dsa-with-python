#kmp algorithm

patt = input("Please enter pattern string\n");
stringMain = input("Please enter Main string\n")

def computeLPS():
    print(patt)
    # Initialize the lps list with zeros
    lps = [0] * len(patt)
    length=0
    i=1
    while i < len(patt):
        if patt[length] == patt[i]:
            length+=1
            lps[i] = length
            i+=1
        else:
            if length!=0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i+=1
    print(lps)
    return lps
            
def patternSearch():
    lpsArr = computeLPS()
    print("lps array:",lpsArr)
    print("Main string:",stringMain)
    length = 0
    i=0
    while i < len(stringMain):
        if(stringMain[i] == patt[length]):
            length+=1
            i+=1
            print("length",length)
            if length == len(patt): return True
        else:
            if length != 0:
                length = lpsArr[length-1]
            else:
                i+=1
    return False


ans = patternSearch()
print("Pattern found: ", ans)