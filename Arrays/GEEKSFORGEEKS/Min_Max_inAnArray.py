class Solution:
    def getMinMax(self, arr):
        #Sourav 
        Min=arr[0]
        Max=arr[0]
        
        for i in range(len(arr)):
            if arr[i]>Max:
                Max=arr[i]
            if arr[i]<Min:
                Min=arr[i]
        return(Min,Max)