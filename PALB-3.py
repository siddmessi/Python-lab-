# ============================================================
# Programming Ability & Logic Building - Week 3
# (02-02-2026 to 07-02-2026)
# All Solutions in GFG Format
# Author: Aanya Chaudhary
# ============================================================


# ============================================================
# 1. Chocolate Distribution Problem
# ============================================================

class Solution1:
    def findMinDiff(self, arr, m):
        n = len(arr)
        if m > n:
            return 0
        
        arr.sort()
        min_diff = float('inf')
        
        for i in range(n - m + 1):
            min_diff = min(min_diff, arr[i + m - 1] - arr[i])
        
        return min_diff


# ============================================================
# 2. Smallest Subarray with Sum Greater than X
# ============================================================

class Solution2:
    def smallestSubWithSum(self, arr, x):
        n = len(arr)
        min_len = float('inf')
        curr_sum = 0
        start = 0
        
        for end in range(n):
            curr_sum += arr[end]
            
            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1
        
        return min_len if min_len != float('inf') else 0


# ============================================================
# 3. Three Way Partitioning
# ============================================================

class Solution3:
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        start = 0
        end = n - 1
        i = 0
        
        while i <= end:
            
            if arr[i] < a:
                arr[i], arr[start] = arr[start], arr[i]
                start += 1
                i += 1
            
            elif arr[i] > b:
                arr[i], arr[end] = arr[end], arr[i]
                end -= 1
            
            else:
                i += 1
        
        return arr


# ============================================================
# 4. Minimum Swaps Required to Bring <= k Together
# ============================================================

class Solution4:
    def minSwap(self, arr, n, k):
        
        count = 0
        for num in arr:
            if num <= k:
                count += 1
        
        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        for i in range(0, n - count):
            if arr[i] > k:
                bad -= 1
            if arr[i + count] > k:
                bad += 1
            
            ans = min(ans, bad)
        
        return ans


# ============================================================
# 5. Palindrome Array
# ============================================================

class Solution5:
    def isPalindrome(self, arr):
        for num in arr:
            if str(num) != str(num)[::-1]:
                return False
        return True


# ============================================================
# 6. Find Median of Array
# ============================================================

class Solution6:
    def find_median(self, arr):
        arr.sort()
        n = len(arr)
        
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n // 2] + arr[n // 2 - 1]) / 2


# ============================================================
# 7. Spiral Traversal of Matrix
# ============================================================

class Solution7:
    def spirallyTraverse(self, matrix, r, c):
        result = []
        top, bottom = 0, r - 1
        left, right = 0, c - 1
        
        while top <= bottom and left <= right:
            
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result


# ============================================================
# 8. Search in 2D Matrix (Binary Search)
# ============================================================

class Solution8:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


# ============================================================
# 9. Median in Row-wise Sorted Matrix
# ============================================================

class Solution9:
    def median(self, matrix, r, c):
        arr = []
        for row in matrix:
            arr.extend(row)
        
        arr.sort()
        return arr[(r * c) // 2]


# ============================================================
# 10. Row with Maximum 1s
# ============================================================

class Solution10:
    def rowWithMax1s(self, arr, n, m):
        max_row = -1
        max_count = 0
        
        for i in range(n):
            count = sum(arr[i])
            if count > max_count:
                max_count = count
                max_row = i
        
        return max_row
