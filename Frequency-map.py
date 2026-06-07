# we find how many time a number came in list and stored value in dictionary or store frequency in dictionary

# Method 1
nums = [1, 2, 3, 3, 4, 1, 5, 7, 9]
frequency_map = {} # also use frequency map = dict()
for i in range(0, len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]] = frequency_map[nums[i]] + 1

    else:
        frequency_map[nums[i]] = 1

print(frequency_map)


#<<<<<<<<<< Method 2 >>>>>>>>>>>

nums = [1, 2, 3, 4, 5, 2, 2, 2, 3, 6]
dic = dict()
n = len(nums)

for i in range(0, n):
    dic[nums[i]] = dic.get(nums[i], 0) + 1

print(dic)