# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Item not found

# Binary Search (Note: List should be sorted)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Item not found

# Example usage
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_item = 7

linear_result = linear_search(my_list, target_item)
binary_result = binary_search(my_list, target_item)

if linear_result != -1:
    print(f"Linear Search: Item {target_item} found at index {linear_result}")
else:
    print(f"Linear Search: Item {target_item} not found")

if binary_result != -1:
    print(f"Binary Search: Item {target_item} found at index {binary_result}")
else:
    print(f"Binary Search: Item {target_item} not found")
