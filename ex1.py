from time import time
from random import randint

# def timed(f):
#     def wrapper(nums, target):
#         start_time = time()
#         result = f(nums, target)
#         end_time = time()
#         print("Search is complete in", end_time - start_time, "sec")
#         return result
#     return wrapper
# @timed

def linear_search(nums: list, target: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] == target:
            return j
        if nums[j] <= target:
            i = j
    return i + 1

def binary_search(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        
        elif target < nums[mid]:
            high = mid - 1
        
        else:
            low = mid + 1


assert linear_search([1, 3, 4, 5], 4) == 2
assert binary_search([1, 3, 4, 5], 4) == 2

large_list_of_numbers = []

while len(large_list_of_numbers) < 10000000:
    new_random_number = randint(100, 999)
    large_list_of_numbers.append(new_random_number)

assert len(large_list_of_numbers) == 10000000

target = large_list_of_numbers[-1]

# Seconds from UNIX Epoch: Jan 1 1970
start = time()
# Run the search function
binary_search(large_list_of_numbers, target)
# Seconds from UNIX Epoch: Jan 1 1970
end = time()
# Calculate the difference between end and start time
diff = end - start
# Print the difference
print("It took", diff, "ms. to find the element")

