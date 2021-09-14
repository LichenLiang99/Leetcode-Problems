class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        #not doable if only one letter
        if len(palindrome) == 1:
            return ""
        
        #check half of the string, replace non 'a' character with 'a'
        #else change last one to 'b'
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        
        return palindrome[:-1] + "b" 
    
    #time o(n) space o(n)