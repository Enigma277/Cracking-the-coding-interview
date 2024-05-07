
def palindromePermutation(s : str) -> bool :
    freq = [0] * 26
    for c in s :
        if(ord('a') <= ord(c) <= ord('z')) :
            #check if this is lowercase english alphabet letter, otherwise ignore
            freq[ord(c) - ord('a')] += 1
    
    odd_char = 0
    for i in range(26) :
        if(freq[i] % 2 == 1):
            odd_char +=1
    
    return odd_char <= 1 # equivalent to return True if odd_char <=1 else False

#Testing our function
print(palindromePermutation("taco cat")) #True
print(palindromePermutation("ababcdc")) #True
print(palindromePermutation("aaabccc")) #False
print(palindromePermutation("aabbcc"))  #True
print(palindromePermutation("aabcdd"))  #False