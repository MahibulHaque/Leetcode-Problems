class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        
        stack=[]
        
        for i in s[0:len(s)]:
            if i=="(" or i=='{' or i=='[':
                stack.append(i)
            elif (i==")" and len(stack)>0):
                poppedChr = stack.pop()
                if poppedChr!="(":
                    return False
                else:
                    continue
            elif (i=="}" and len(stack)>0):
                poppedChr = stack.pop()
                if poppedChr!="{":
                    return False
                else:
                    continue
            elif (i=="]" and len(stack)>0):
                poppedChr = stack.pop()
                if poppedChr!="[":
                    return False
                else:
                    continue
            else:
                return False
        
        if len(stack)>0:
            return False
            
        return True