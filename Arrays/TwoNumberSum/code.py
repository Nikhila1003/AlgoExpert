#Solution 1 / Naive Approach
# O(n^2), space complexity - O(1)
def twoNumberSum(array, targetSum):
    for index1 in range(len(array)):
        for index2 in range(index1 + 1, len(array)):
            if array[index1] + array[index2] == targetSum:
                return [array[index1], array[index2]]                
    return []


#Solution 2 
# O(nlogn), space complexity - O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left_ptr = 0 
    right_ptr = len(array) - 1
    while left_ptr < right_ptr:
        sum = array[left_ptr] + array[right_ptr]
        if sum == targetSum:
            return [array[left_ptr], array[right_ptr]]
        elif sum < targetSum:
            left_ptr = left_ptr + 1
        else:
            right_ptr = right_ptr - 1
    return []


#Solution 3
# O(n), space complexity - O(n)
def twoNumberSum(array, targetSum):
    upd = {}
    for i in range(len(array)):
        res = targetSum - array[i]
        if res in upd:
            return [array[i], res] 
        upd[array[i]] = 1
    return []
