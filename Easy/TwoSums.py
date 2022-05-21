class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsDict = {}
        res=[]
        for i in range(0,len(nums)):
            if(target-nums[i] in numsDict.keys()):
                return [numsDict[target-nums[i]], i]
            else:
                numsDict[nums[i]] = i