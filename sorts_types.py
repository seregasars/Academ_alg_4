import random

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       pivot = random.choice(nums)
   less_nums = [n for n in nums if n < pivot]
 
   p_nums = [pivot] * nums.count(pivot)
   bigger_nums = [n for n in nums if n > pivot]
   return quicksort(less_nums) + p_nums + quicksort(bigger_nums)

def comb(nums):
	gap = len(nums)
	swaps = True
	while gap > 1 or swaps:
		gap = max(1, int(gap / 1.25)) 
		swaps = False
		for i in range(len(nums) - gap):
			j = i + gap
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i]
				swaps = True
	return nums

def bucket(nums):
    max_value = max(nums)
    size = max_value/len(nums)

    buckets_list= []
    for x in range(len(nums)):
        buckets_list.append([]) 

    for i in range(len(nums)):
        j = int (nums[i] / size)
        if j != len (nums):
            buckets_list[j].append(nums[i])
        else:
            buckets_list[len(nums) - 1].append(nums[i])

    for z in range(len(nums)):
        quicksort(buckets_list[z])

    final_output = []
    for x in range(len (nums)):
        final_output = final_output + buckets_list[x]
    return final_output

def heap(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums

def heapify(nums, heap_size, root_index):  
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
        
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

