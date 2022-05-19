class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        firstStrDict = {}
        
        for i in s[0:len(s)]:
            if(i not in firstStrDict.keys()):
                firstStrDict[i] = 1
            else:
                firstStrDict[i] = firstStrDict[i]+1
        
        for j in t[0: len(t)]:
            if (j not in firstStrDict.keys()):
                return False
            elif(j in firstStrDict.keys() and (firstStrDict[j]<=0)):
                return False
            else:
                firstStrDict[j]-=1
        return True