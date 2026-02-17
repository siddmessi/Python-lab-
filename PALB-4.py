"""
School of Computer Science and Engineering
Programming Ability and Logic Building - 1
Week: 09/02/2026 to 14/02/2026

All Experiments - Python Version
"""

# ==========================================================
# 1. Search Insert Position
# ==========================================================

def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


# ==========================================================
# 2. Combination Sum
# ==========================================================

def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


# ==========================================================
# 3. Combination Sum II
# ==========================================================

def combination_sum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


# ==========================================================
# 4. Jump Game II
# ==========================================================

def jump_game_ii(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


# ==========================================================
# 5. Group Anagrams
# ==========================================================

def group_anagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())


# ==========================================================
# 6. Plus One
# ==========================================================

def plus_one(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


# ==========================================================
# 7. Set Matrix Zeroes
# ==========================================================

def set_matrix_zeroes(matrix):
    rows = set()
    cols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0


# ==========================================================
# 8. Search 2D Matrix
# ==========================================================

def search_matrix(matrix, target):
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        value = matrix[mid // n][mid % n]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# ==========================================================
# 9. Sort Colors
# ==========================================================

def sort_colors(nums):
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ==========================================================
# 10. Subsets
# ==========================================================

def subsets(nums):
    result = [[]]

    for num in nums:
        result += [curr + [num] for curr in result]

    return result


# ==========================================================
# 11. Word Search
# ==========================================================

def word_search(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        if index == len(word):
            return True

        if (r < 0 or c < 0 or
            r >= rows or c >= cols or
            board[r][c] != word[index]):
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))

        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


# ==========================================================
# 12. 4Sum
# ==========================================================

def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


# ==========================================================
# 13. Search in Rotated Sorted Array
# ==========================================================

def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# ==========================================================
# 14. Find First and Last Position in Sorted Array
# ==========================================================

def search_range(nums, target):
    def find_first():
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def find_last():
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    return [find_first(), find_last()]
