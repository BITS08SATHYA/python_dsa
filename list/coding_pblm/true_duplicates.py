def contains_duplicates(nums):

    if not nums:
        return

    hashMap = {}

    count = 1
    for i in range(len(nums)):
        if nums[i] in hashMap:
            hashMap[count] += 1
        else:
            hashMap[nums[i]] = 1

    if hashMap[count] == 2:
        return True
    return False

print(contains_duplicates([2, 1, 1, 4]))