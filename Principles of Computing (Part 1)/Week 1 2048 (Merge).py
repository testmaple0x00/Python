"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result=[0]*len(line)
    count=0
    firstfind=None
    for index in range(len(line)):
        #try to find first nonzero
        while count<len(line):
            if line[count]!=0:
                #temp first number
                #compare second number to merge or not
                if firstfind==None:
                    firstfind=line[count]
                else:
                    if firstfind==line[count]:
                        result[index]=firstfind*2
                        firstfind=None
                    else:
                        result[index]=firstfind
                        firstfind=line[count]
                    count+=1
                    break
            count+=1
        if count==len(line) and result[index]==0:
            if firstfind!=None:
                result[index]=firstfind
            else:
                result[index]=0
            count+=1
        elif count>len(line):
            result[index]=0
    return result
