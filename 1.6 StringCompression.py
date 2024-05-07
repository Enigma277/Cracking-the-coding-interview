def compressString(s : str) -> str:
    currentCount = 1
    currentChar = s[0]
    compressedString = []

    for i in range(1, len(s)) :
        if(s[i] == currentChar):
            currentCount += 1
        else:
            compressedString.append(currentChar)
            compressedString.append(str(currentCount))
            currentCount = 1
            currentChar = s[i]
    
    compressedString.append(currentChar)
    compressedString.append(str(currentCount))

    compressedString = ''.join(compressedString)

    if(len(compressedString) >= len(s)) :
        return s
    return compressedString

#Testing our function
print(compressString("aabcccccaaa")) #a2b1c5a3
print(compressString("abbccad"))  # since len(a1b2c2a1d1) > len(abbccad) thus it will return original string
