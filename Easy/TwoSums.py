class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        res=[]
        for i in range(0,len(nums)):
            if(target-nums[i] in numsDict.keys()):
                return [numsDict[target-nums[i]], i]
            else:
                numsDict[nums[i]] = i