'''
Given two string , check if one of them is permutation of other.
'''

'''
Approach 1 :
sort both strings and if they both are representing same permutation of
characters then their sorted version will be equal
TC: O(nlog(n)) where n is the length of both the strings
SC: O(1)
'''
def checkPermutation1(s : str, t:str) -> bool:
    if(len(s) != len(t)) : #micro optimization to bypass all cases
        return False       #where strings are not of same length

    s = sorted(s)
    t = sorted(t)
    return s==t # return True if s==t else return False

'''
Approach 2:

create a frequency array to store the freq of each char in s, now if one
of them is permutation of other then their freq count will be equal for every
char. we are incrementing the freq for s and decrementing the freq for t so if both
of them have same freq then result should be 0.

TC: O(n)
SC: O(256)
'''
def checkPermutation2(s : str, t: str) -> bool:
    if(len(s) != len(t)) :
        return False
    
    freq = [0] * 256
    for c in s:
        freq[ord(c)] += 1
    
    for c in t:
        freq[ord(c)] -= 1
    
    for i in range(256) :
        if (freq[i] != 0):
            return False
        
    return True

#Testing our function
print(checkPermutation1("abdbd", "bbdda")) # should return True
print(checkPermutation1("abca", "aab")) # should return False
print(checkPermutation1("aabbcc", "abbbcc")) #should return False

print(checkPermutation2("abdbd", "bbdda")) # should return True
print(checkPermutation2("abca", "aab")) # should return False
print(checkPermutation2("aabbcc", "abbbcc")) #should return False