"""
School of Computer Science and Engineering
Programming Ability and Logic Building - 1
All Array Experiments (In-Class + Take Home)
Language: Python
"""
# ---------------------------------------------------
# 1. Reverse an Array (Modify In-Place)
# ---------------------------------------------------

class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr


# ---------------------------------------------------
# 2. Find Minimum and Maximum in Array
# ---------------------------------------------------

class Solution:
    def getMinMax(self, arr):
        minimum = arr[0]
        maximum = arr[0]
        
        for num in arr:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
        
        return [minimum, maximum]


# ---------------------------------------------------
# 3. Kth Smallest Element
# ---------------------------------------------------

class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k - 1]


# ---------------------------------------------------
# 4. Union of Two Arrays
# ---------------------------------------------------

class Solution:
    def findUnion(self, a, b):
        return list(set(a) | set(b))


# ---------------------------------------------------
# 5. Largest Element in Array
# ---------------------------------------------------

class Solution:
    def largest(self, arr):
        largest = arr[0]
        
        for num in arr:
            if num > largest:
                largest = num
        
        return largest


# ---------------------------------------------------
# 6. Rotate Array by One (Clockwise)
# ---------------------------------------------------

class Solution:
    def rotate(self, arr):
        if len(arr) == 0:
            return arr
        
        last = arr[-1]
        
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        
        arr[0] = last
        return arr


# ---------------------------------------------------
# 7. Maximum Subarray Sum (Kadane’s Algorithm)
# ---------------------------------------------------

class Solution:
    def maxSubArraySum(self, arr):
        max_current = arr[0]
        max_global = arr[0]
        
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            max_global = max(max_global, max_current)
        
        return max_global


# ---------------------------------------------------
# 8. Search Insert Position (Binary Search)
# ---------------------------------------------------

class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left


# ---------------------------------------------------
# 9. Two Sum
# ---------------------------------------------------

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i


# ---------------------------------------------------
# 10. Minimum Number of Jumps
# ---------------------------------------------------

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        if n <= 1:
            return 0
        
        if arr[0] == 0:
            return -1
        
        max_reach = arr[0]
        step = arr[0]
        jump = 1
        
        for i in range(1, n):
            if i == n - 1:
                return jump
            
            max_reach = max(max_reach, i + arr[i])
            step -= 1
            
            if step == 0:
                jump += 1
                
                if i >= max_reach:
                    return -1
                
                step = max_reach - i
        
        return -1
