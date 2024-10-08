# Binary Search algorithm implementation in Python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
array = [2, 3, 4, 10, 40]
target = 10
result = binary_search(array, target)
print("Element found at index:", result if result != -1 else "Element not found")
