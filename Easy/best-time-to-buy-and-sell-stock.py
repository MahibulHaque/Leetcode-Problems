
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices)==1:
            return 0
        
        left_pointer = prices[0]
        right_pointer = 0
        max_profit=0
        for i in range(1,len(prices)):
            
            right_pointer =  prices[i]
            if right_pointer<left_pointer:
                left_pointer = prices[i]
                i+=1
            elif left_pointer<right_pointer:
                max_profit = max(max_profit, (right_pointer-left_pointer))
        
        return max_profit