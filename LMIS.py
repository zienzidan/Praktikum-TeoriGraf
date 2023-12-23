# Return length of LIS in arr[] of size N
# Complexity (NlogN)

def lis(arr) : 
    s = set()
    for i in range (len(arr)) :

        # Check if the element was actually inserted
        # An element in set is not inserted if it is
        # already present
        if arr[i] not in s :
            s.add(arr[i])

            # Find the position of inserted element
            # Find the next greater element in set
            next_greater = [x for x in s if x > arr[i]]

            # If the new element is not inserted at the end, then
            # remove the greater element next to it
            if next_greater :
                s.remove(min(next_greater))
    return len(s)

arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
print(lis(arr)) 