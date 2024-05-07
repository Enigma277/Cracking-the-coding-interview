def stringRotation(s : str, t: str) -> bool :
    s = s+s
    return t in s #equivalent to if(isSubstring(t, s)) == True return True else return False

#Testing our function
print(stringRotation("waterbottle", "erbottlewat"))