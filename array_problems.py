# Arrays Problems:

# 1. Reverse an Array
arr=[1,2,3,4,5]
arr1=[]
for i in range(len(arr)):
    a=arr.pop()
    arr1.append(a)
print(arr1,"\n")


# 2. Find the Maximum & Minimum Element
arr=[1,2,3,4,5,6]
for i in range(len(arr)):
    maximum=arr[0]
    minimum=arr[0]
    if arr[i]>arr[i-1]:
        maximum=arr[i]
    if arr[i]<arr[i-1]:
        minimum=arr[i]
print("maximum:",maximum)
print("minimum:",minimum,"\n")

# 3. Find the Sum of Elements
arr=[1,2,3,4,5,6]
total=0
for i in range(len(arr)):
    total+=arr[i]
print(total,"\n")

# 4. Find the Second Largest Element
arr = [1, 2, 3, 4, 5]
arr=list(set(arr))
arr.sort(reverse=True)
print(arr[1],"\n")

# 5. Count Frequency of Elements
arr = [1, 2, 2, 3, 1, 4, 2]
for x in set(arr):
    print(x,":",arr.count(x))
print()

# 6. Check if Array is Sorted
arr = [1, 2, 3, 6, 5]
if arr==sorted(arr):
    print("Array is sorted")
else:
    print("Array is not sorted")
print()

# 7. Rotate Array by k Positions: Rotate the array to the right by k positions.
arr = [1, 2, 3, 6, 5]
k=2
k = k % len(arr)
rotated=arr[-k:]+arr[:-k]
print(rotated)
print()

# 8. Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.
arr = [1, 2, 3, 6, 5]
target_sum = 6

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == target_sum:
            print("Pair found:", arr[i], arr[j])
print()

# 9. Remove Duplicates from Array: Remove duplicates from the array while maintaining order.
arr = [1, 2, 2, 5, 1, 4, 2]
arr1=[]
for i in arr:
    if i in arr1:
        continue
    else:
        arr1.append(i)
print(arr1)
print()

# 10. Merge Two Sorted Arrays
arr1=[1,3,5]
arr2=[2,4,6]
arr=arr1+arr2
print(sorted(arr))
print()

# 11. Remove given Element from Array
arr=[1,2,3,4,5]
el=4
for x in arr:
    if x==el:
        arr.remove(el)
print(arr)
print()

# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.
arr=[1,2,4,5]
n=5
exp_sum=n*(n+1)//2
summ=0
for x in arr:
    summ+=x
num=exp_sum-summ
print(num)
print()

# 13. Find Duplicates in an Array
arr = [1, 2, 2, 5, 1, 4, 2]
seen_elements=set()
duplicates=set()
for x in arr:
    if x in seen_elements:
        duplicates.add(x)
    else:
        seen_elements.add(x)
print(list(duplicates))
print()

# 14. Find Intersection of Two Arrays: Find the common elements between two arrays.
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 5]
intersection_arr=set(arr1) & set(arr2)
print("intersection: ",list(intersection_arr))
print()

# 15. Find Union of Two Arrays
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 4, 5, 6]
union_arr=set(arr1) | set(arr2)
print("union: ",list(union_arr))
print()

# 16. Check if Two Arrays Are Equal: if two arrays contain the same elements
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
if arr1 == arr2:
    print("Arrays are equal")
else:
    print("Arrays are not equal")
print()

# 17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.
arr = [16, 17, 4, 3, 5, 2]
for i in range(len(arr)):
    leader=True
    for j in range(i+1,len(arr)):
        if arr[i]<=arr[j]:
            leader=False
            break
    if leader:
        print(arr[i]) 
print()

# 18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
arr = [0, 3, 0, 1, 12]
arr1=[]
for i in arr:
    if i!=0:
        arr1.append(i)
zeroes = arr.count(0)
for i in range(zeroes):
    arr1.append(0)

print("Result is:",arr1)
print()

# 19. Find Subarray with Given Sum.
arr = [1, 4, 10, 3, 12, 20, 5]
target = 25
for i in range(len(arr)):
    summ = 0
    for j in range(i, len(arr)):
        summ += arr[j]
        if summ == target:
            print("Subarray:", arr[i:j+1])
            break
print()

# 20. Rotate Array to the Left by k Positions
arr = [1, 2, 3, 6, 5]
k=3
k=k % len(arr)
rotated=arr[k:]+arr[:k]
print(rotated)
print()

# 21. Find the Kth Smallest Element
arr = [7, 10, 4, 3, 20, 15]
k = 2
arr.sort()
print("Kth smallest element:", arr[k-1])
print()

# 22. Find All Subarrays
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i:j+1])
print()

# 23. arr = [-2, -1, -3, 4, 1, 2, 1, 5, 4]
max_sum = 0
summ = 0
for i in arr:
    summ = summ + i
    if summ < 0:
        summ = 0
    if summ > max_sum:
        max_sum = summ
print("Maximum sum:", max_sum)
print()

# 24. Rearrange Array Alternately: Rearrange an array such that elements alternate between the largest and smallest.
arr = [1, 6, 3, 5, 4, 2]
arr.sort()  
result = []
while arr:
    result.append(arr[-1]) 
    arr.pop()              
    if arr:
        result.append(arr[0]) 
        arr.pop(0)             
print("Rearranged array:", result)
print()

# 25. Find Majority Element: Find the element that appears more than n/2 times.
arr = [3, 3, 4, 2, 3, 3, 3]
found = False

for num in arr:
    if arr.count(num) > len(arr) // 2:  # check if count is more than n/2
        print("Majority element is:", num)
        found = True
        break

if not found:
    print("No majority element")
print()

# 26. Find Peak Element: A peak element is greater than its neighbors. Find one such element.
arr = [2, 3, 10, 4, 5, 0]
n = len(arr)

for i in range(n):
    if i == 0 and arr[i] > arr[i+1]:
        print("Peak element is:", arr[i])
        break
    elif i == n-1 and arr[i] > arr[i-1]: 
        print("Peak element is:", arr[i])
        break
    elif 0 < i < n-1 and arr[i] > arr[i-1] and arr[i] > arr[i+1]: 
        print("Peak element is:", arr[i])
        break
print()

# 27. arr = [2, 5, 6, 1]
i = 1
for i in range(1,len(arr)+1):
    if i not in arr:
        print("First missing positive:", i)
        break
    i += 1
print()

# 28. Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.
arr = [0, 2, 1, 1, 0, 1, 0]
count0 = arr.count(0)
count1 = arr.count(1)
count2 = arr.count(2)
arr = [0]*count0 + [1]*count1 + [2]*count2
print(arr)
print()

# 29. Find the Longest Consecutive Sequence: Find the length of the longest consecutive sequence of integers.
arr = [100, 4, 200, 1, 3, 2]

arr.sort()  # sort the array
longest = 1
current = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i-1] + 1:  # consecutive
        current += 1
    elif arr[i] != arr[i-1]:    # not consecutive
        current = 1
    longest = max(longest, current)  # works now

print("Length of longest consecutive sequence:", longest)
print()

# 30. Product of Array Except Self
# Given an array, return a new array where each element is the product of all elements except itself.
arr = [1, 2, 3, 4]
result = []
for i in range(len(arr)):
    prod = 1
    for j in range(len(arr)):
        if i != j:
            prod *= arr[j]
    result.append(prod)
print(result)
print()


# 31. Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.
arr = [4, 1, 5, 2, 3]
found = False

for i in range(len(arr)):
    left = sum(arr[:i])
    right = sum(arr[i+1:])
    if left == right:
        print("Equilibrium index:", i)
        found = True
        break

if not found:
    print("No equilibrium index found")
print()

# 32. arr = [1, -9, 3, 6, 8, -2]

# Step 1: Sort the array
arr.sort()

# Step 2: Compare product of first two and last two
if arr[0]*arr[1] > arr[-1]*arr[-2]:
    print("Maximum product pair:", (arr[0], arr[1]))
    print("Maximum product:", arr[0]*arr[1])
else:
    print("Maximum product pair:", (arr[-2], arr[-1]))
    print("Maximum product:", arr[-1]*arr[-2])
print()

# 33. arr = [2, 3, 10, 6, 4, 8, 1]
min_val = arr[0]
max_diff = arr[1] - arr[0]
for i in range(1, len(arr)):
    diff = arr[i] - min_val
    if diff > max_diff:
        max_diff = diff
    if arr[i] < min_val:
        min_val = arr[i]
print("Maximum difference:", max_diff)










