# Hashing is basically prestoring the value in some datastructure like list / dictionar / sets and fetching it

n = [5, 3, 2, 2, 1, 5, 5, 7, 10]
m = [10, 111, 1, 9, 5, 67, 2]

hash_list = [0] * 11  # use this extra datastructure with length 11 and with 0 value at each index initially

for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])