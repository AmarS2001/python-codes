class Solution:
    def reverse(self, x: int) -> int:
        if  x < -2**31 and x>2**31:
            return 0
        num=abs(x)
        ans=0
        while(num>0):
            ans=(ans*10)+ num%10
            num=num//10
        if x<0:
            ans= 0-ans
        if ans > 2**31:
            return 0
        if ans < -2**31:
            return 0
        return ans
            
