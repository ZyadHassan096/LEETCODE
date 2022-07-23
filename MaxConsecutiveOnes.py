# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:55:10 2022

@author: ROG
"""




class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
      
        tempcount = 0
        total= 0
        
        for i in nums:
            if i == 1:
                tempcount = tempcount +1
                if total <= tempcount:
                    total = tempcount
            else:
                tempcount = 0 
        return total
            
   
    
    
    
    


new = Solution()

print(new.findMaxConsecutiveOnes([1,0,1,1,0,1]))
    


            
            
    