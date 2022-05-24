class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens)==1:
            return tokens[0]
        
        
        numStack = []
        
        for i in tokens[0:len(tokens)]:
            if i=="+" or i=="-" or i=="*" or i=="/":

                firstNum = numStack.pop()
                secondNum = numStack.pop()
                
                if i=='+':
                    numStack.append(secondNum+firstNum)
                elif i=='-':
                    numStack.append(secondNum-firstNum)
                elif i=="*":
                    numStack.append(secondNum*firstNum)
                elif i=="/":
                    numStack.append(int(secondNum/firstNum))
            else:
                numStack.append(int(i))
        
        if len(numStack)==1:
            return numStack[0]