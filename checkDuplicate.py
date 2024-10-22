def checkDuplicate(nums):
    hashset = set()
    
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

nums = [5, 6, 7, 8, 9]
result = checkDuplicate(nums)
print(result)  # output shoud be False
