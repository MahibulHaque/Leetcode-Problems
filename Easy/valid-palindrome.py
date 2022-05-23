class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        
        if (len(s)<=1):
            return True        
        s = s.lower()
        l=0
        r=0
        for i in range(0,len(s)):
            l=i
            r=len(s)-1-i
            
            if(l<=r):
                if(s[l]==s[r]):
                    continue
                else:
                    return False
            else:
                break
        return True