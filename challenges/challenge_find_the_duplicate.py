def find_duplicate(nums):
    if (
        not nums
        or not isinstance(nums, list)
        or not all(isinstance(num, int) and num > 0 for num in nums)
    ):
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False

# nums = [1, -2, 3, 4, -4, 5]
# result = find_duplicate(nums)
# print(result)
