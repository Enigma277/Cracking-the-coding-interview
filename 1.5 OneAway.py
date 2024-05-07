
def oneAway(s : str, t : str) -> bool:
    if(len(s) == len(t)) :
        return isOneEditAway(s, t)
    if(len(s) == len(t) + 1) :
        return isOneInsertAway(t, s)
    if(len(s) + 1 == len(t)) :
        return isOneInsertAway(s, t)

def isOneEditAway(s : str, t: str) -> bool:
    editRequired = 0
    for i in range(len(s)) :
        if(s[i] != t[i]):
            editRequired += 1
            if(editRequired > 1) :
                return False
    return True

#check if we can insert one char in s to get t
def isOneInsertAway(s : str, t: str) -> bool:
    i, j = 0, 0
    insertRequired = 0
    while(i < len(s) and j < len(t)) :
        if(s[i] != t[j]):
            insertRequired += 1
            #since we are inserting in s thus current char of s will now be matched with next char of t,
            #thus, only incrementing index of second string t
            j+=1           
            if(insertRequired > 1) :
                return False
        else :
            i+=1
            j+=1
    return True

#Testing our function
print(oneAway("pale", "ple")) #True
print(oneAway("pales", "pale")) #True
print(oneAway("pale", "bale")) #True
print(oneAway("pale", "bae")) #False