def binary_search(list_of_nums, num):
    first_index = 0
    last_index = len(list_of_nums) - 1
    found = False

    while (first_index <= last_index and found != True):
        mid_index = (first_index + last_index) // 2
        if list_of_nums[mid_index] == num:
            found = True
        else:
            if num < list_of_nums[mid_index]:
                last_index = mid_index - 1
            else:
                first_index = mid_index + 1
    return found

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))
