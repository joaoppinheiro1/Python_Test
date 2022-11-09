# -*- coding: utf-8 -*-
'''Breve descrição do problema:by leetcode.com
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''


nums = [2,5,3]
target = 10

class Solution(object):
    def two_sum(self, nums, target):
        
        output = []
        aux1 = 0
        aux2 = 0
        
        for i in range(len(nums)):
            aux1 = nums[i]
            for l in range(i + 1, len(nums)):
                aux2 = nums[l]
                aux2 = aux2 + aux1
                if aux2 == target:
                    output.append(i)
                    output.append(l)
                    
        print(output)

solution = Solution()
solution.two_sum(nums, target)
      