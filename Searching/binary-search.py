def binary_search(list_of_nums, num):
    list_of_nums = sorted(list_of_nums)
    first_index = 0
    last_index = len(list_of_nums) - 1
    found = False
    
    while (first_index <= last_index and found != True):
        # if you don't do //, then mid_index might not be an integer
        mid_index = (first_index + last_index) // 2
        if list_of_nums[mid_index] == num:
            found = True
        else:
            if num < list_of_nums[mid_index]:
                # last_index can't be mid_index. because we already know list_of_nums[mid_index] isn't the num
                last_index = mid_index - 1
            else:
                # same thing
                first_index = mid_index + 1
    return found

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))
