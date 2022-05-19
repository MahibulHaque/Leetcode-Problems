
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool :
        numsDict={}
        for i in nums[0:len(nums)]:
            if(i in numsDict.keys()):
                return True
            else:
                numsDict[i] = True

        return False