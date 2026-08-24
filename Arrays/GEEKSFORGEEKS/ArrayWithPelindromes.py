class Solution:
    def isPalinArray(self, arr):
        
        # code here
        for nums in arr:
            original=nums
            rev=0
            
            while nums>0:
                digit=nums%10
                rev=rev*10+digit
                nums//=10
            if rev!=original:
                return False
        return True        
            