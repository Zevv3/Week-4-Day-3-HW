# Your goal in this kata is to implement a difference function, 
# which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present 
# in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must
#  be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]
#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff_Original(a, b):
    for x in range(len(a)):
        for i in a:
            while i in a:
                if i in b:
                    a.remove(i)
                else:
                    break
        
    
    return a
print(array_diff_Original([1,2,3], [1, 2]))

def array_diff_Updated(a,b):
    result = []
    for num in a:
        if num not in b:
            result.append(num)
    return result
print(array_diff_Updated([1,2,3], [1, 2]))

def array_diff_listcomp(a,b):
    return [num for num in a if num not in b]

print(array_diff_listcomp([1,2,3], [1, 2]))
