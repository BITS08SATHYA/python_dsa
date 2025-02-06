# Question 2 - Find Pairs
# LeetCode - 1 - Two Sum

def findPairs(nums, target):
    list = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                list.append((i,j))
    return list



print(findPairs([1, 2, 3, 2, 3, 4, 5, 6], 6))