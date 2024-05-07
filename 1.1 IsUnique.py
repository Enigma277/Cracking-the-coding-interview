'''
Implement an algorithm to determine if a string has all
unique characters 
'''

'''
Approach 1 : 

Assuming the string can take any of the 256 allowed character.
Create a frequency array and return false if any of the character has
freaquency > 1 otherwise return true

Time Complexity: O(min(256, len(s))
Space Complexity: O(256) 
'''
def isUnique1(s : str) -> bool :
    freq = [0] * 256
    for c in s :
        freq[ord(c)] += 1
        if(freq[ord(c)] > 1):
            return False
    return True

'''
Approach 2 :

If we don't want to use extra space then for every character we can iterate if
we have found this character before or not.

The approach is O(n^2) in time but as any string which has more than 256
character will definetely return false at 257th iteration in worst case thus
Time complexity will be O(256 * 256) and space complexity will be O(1)
'''

def isUnique2(s : str) -> bool :
    for i in range(len(s)) :
        if s[i] in s[0:i]:
            return False
    return True

#Testing our function
print(isUnique1("abcdef")) #should print True
print(isUnique1("aba")) #should print False
print(isUnique2("abcdef")) #should print True
print(isUnique2("aba")) #should print False