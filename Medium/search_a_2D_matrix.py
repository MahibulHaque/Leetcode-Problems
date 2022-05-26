class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            l=0
            h=len(row)-1
            
            while(l<=h):
                mid = (l+h)//2
                
                if(row[mid]==target):
                    return True
                elif(row[mid]<target):
                    l=mid+1
                elif(row[mid]>target):
                    h=mid-1
        return False