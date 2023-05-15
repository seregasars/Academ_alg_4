import sorts_types, random

nums = [random.randint(1, 100) for i in range(20)]
print('Исходный список: ', nums)
print()
print('Блочная сортировка: ', sorts_types.bucket(nums))
print()
print('Пирамидальная сортировка: ', sorts_types.heap(nums))