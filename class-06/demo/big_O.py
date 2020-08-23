# Measure # of operations
n = 7 #1 operation 
for i in range(n):
  print(i) # n operations

# n+1 operations

# n = 5 > 6
# n = 100 > 101
# n = 1000000 > 1000001
# O(n+1)
# O(n)


def testing_bigoh(n):
  for i in range(n):
    for j in range(n):
      print(i,j) # n*n (n^2)

# testing_bigoh(8)

# O(n^2)



nums1 = [2, 5, 8, 9, 43, 7]
nums2 = [-4, 43, 7, 8, 13, 45]

# One Loop
# Return a list of all items bigger than number in unsorted list
def find_nums_above(nums_list, number):
  result = [] # 1 operation
  for num in nums_list: # n times
    if num > number:
      result.append(num) # 1 operation -- 1 extra space
    elif num < number:
      print("Less")
    else:
      print("Else") 
    print("Done with current iteration") # 1 operation
  return result # 1 operation
  
print(find_nums_above(nums1, 10))

# O(2*n+1+1) => O(2n+2)
# O(n)
# O(n) spaces


def find_nums_above_loop_inside(nums_list, number):
  result = [] # 1 operation
  for num in nums_list: # n times
    if num > number:
      result.append(num) # 1 operation
    elif num < number:
      print("Less") # 1 op
      for j in range(len(nums_list)): # n times
        print("Just for fun") # 1 op
    else:
      print("Else") # 1 op
    print("Done with current iteration") # 1 operation
  return result # 1 operation
  
# O(1 + n (1+   (1 or 1+n or 1)  ) + 1)
# O(1 + n (1+ 1+n) + 1)
# O(1 + n(2+n) +1)
# O(2 + 2n^2)
# O(2n^2)
# O(n^2)


print(find_nums_above_loop_inside(nums1, 10))



def tricky_example(a):
  print("Hi") # 1 op
  print (3*4*6/2) # 1 op
  a.sort() # Hidden loop (n*log(n)) -- Merge sort
  print(a) # 1 op
  print("The end") # 1 op

# O(4 + sort-big-oh)
# O(sort-big-oh)
a = [4,7,2,9,5,0,3]



# Binary Search
# O(log n)
# We divide the array into two halfes and we elimate one of them
sorted_list = [-1, 4, 6, 9, 23, 30, 45, 65, 76, 77, 90]

def binary_search(sorted_nums, target):
  min = 0 # 1 space
  max = len(sorted_nums)-1 # 1 space
  while max>min:
    pivot = (max+min)//2 # 1 space
    print(max, min, pivot)
    if target == sorted_nums[pivot]:
      return pivot
    elif target < sorted_nums[pivot]:
      max = pivot-1
    else:
      min = pivot+1
  return -1

print(binary_search(sorted_list, -1))

# O(3) spaces
# O(1) 

# O(3*log n ) spaces
# O(log n)


def fib(i):
  # base cases
  return fib(i-1) + fib(i-2)


# fib(4) = fib(3) + fib(2)
# We recreate i variable in every recursive call





