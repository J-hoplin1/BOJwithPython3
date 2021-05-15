def solution(nums):
    answer = 0
    totalTypes = list(set(nums))
    maxSelect = int(len(nums) / 2)
    if len(totalTypes) >= maxSelect:
        return maxSelect
    else:
        return len(totalTypes)
