# ============================================================
# Programming Ability & Logic Building
# All Solutions in GFG Format
# Author:Siddharth
# ============================================================


# ============================================================
# 1. Kth Smallest Element
# ============================================================

class Solution1:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k - 1]


# ============================================================
# 2. Minimize the Heights
# ============================================================

class Solution2:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[-1] - arr[0]
        smallest = arr[0] + k
        largest = arr[-1] - k
        
        for i in range(n - 1):
            min_val = min(smallest, arr[i + 1] - k)
            max_val = max(largest, arr[i] + k)
            
            if min_val < 0:
                continue
            
            ans = min(ans, max_val - min_val)
        
        return ans


# ============================================================
# 3. Minimum Number of Jumps
# ============================================================

class Solution3:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0
        
        if arr[0] == 0:
            return -1
        
        maxReach = arr[0]
        step = arr[0]
        jump = 1
        
        for i in range(1, n):
            
            if i == n - 1:
                return jump
            
            maxReach = max(maxReach, i + arr[i])
            step -= 1
            
            if step == 0:
                jump += 1
                
                if i >= maxReach:
                    return -1
                
                step = maxReach - i
        
        return -1


# ============================================================
# 4. Find the Duplicate Number (Floyd's Cycle)
# ============================================================

class Solution4:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


# ============================================================
# 5. Merge Two Sorted Arrays Without Extra Space
# ============================================================

class Solution5:
    def merge(self, a, b, n, m):
        gap = (n + m + 1) // 2
        
        while gap > 0:
            i = 0
            j = gap
            
            while j < (n + m):
                
                if j < n and a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                
                elif i < n and j >= n and a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]
                
                elif i >= n and b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]
                
                i += 1
                j += 1
            
            if gap == 1:
                gap = 0
            else:
                gap = (gap + 1) // 2


# ============================================================
# 6. Merge Intervals
# ============================================================

class Solution6:
    def merge(self, intervals):
        intervals.sort()
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


# ============================================================
# 7. Common Elements in 3 Sorted Arrays
# ============================================================

class Solution7:
    def commonElements(self, A, B, C):
        i = j = k = 0
        n1, n2, n3 = len(A), len(B), len(C)
        result = []
        
        while i < n1 and j < n2 and k < n3:
            
            if A[i] == B[j] == C[k]:
                if not result or result[-1] != A[i]:
                    result.append(A[i])
                i += 1
                j += 1
                k += 1
            
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        
        return result if result else [-1]


# ============================================================
# 8. Factorial of Large Number
# ============================================================

class Solution8:
    def factorial(self, N):
        result = 1
        for i in range(2, N + 1):
            result *= i
        return list(map(int, str(result)))


# ============================================================
# 9. Array Subset of Another Array
# ============================================================

class Solution9:
    def isSubset(self, a, b):
        from collections import Counter
        
        countA = Counter(a)
        countB = Counter(b)
        
        for key in countB:
            if countB[key] > countA.get(key, 0):
                return False
        
        return True


# ============================================================
# 10. Triplet Sum in Array
# ============================================================

class Solution10:
    def find3Numbers(self, arr, target):
        arr.sort()
        n = len(arr)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return False


# ============================================================
# 11. Trapping Rain Water
# ============================================================

class Solution11:
    def trappingWater(self, arr, n):
        if n == 0:
            return 0
        
        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        water = 0
        
        while left <= right:
            
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water += right_max - arr[right]
                right -= 1
        
        return water
