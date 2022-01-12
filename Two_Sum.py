class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
    
        for i in range(0,len(nums)):
            a=nums[i]
            b=target-a
    
            if a+b == target and b in nums and i!=nums.index(b):
                lis.append(i)
                lis.append(nums.index(b))
                break
                
        return lis
