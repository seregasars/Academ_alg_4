import sorts_types, random, timeit

nums = [random.randint(1, 100) for i in range(20)]
print(nums)
print()
ans = str(input('Введите "q" для быстрой сортировки, "c" для сортировки расческой или "a" для сравнения видов сортировки '))
print()

if ans == 'q':
    start_time = timeit.default_timer()
    print(sorts_types.quicksort(nums))
    print('Время: ', timeit.default_timer() - start_time)
elif ans == 'c':
    start_time = timeit.default_timer()
    print(sorts_types.comb(nums))
    print('Время: ', timeit.default_timer() - start_time)
else:
    print('Быстрая сортировка:')
    start_time = timeit.default_timer()
    print(sorts_types.quicksort(nums))
    print('Время: ', timeit.default_timer() - start_time)
    print()
    print('Сортировка расческой:')
    start_time = timeit.default_timer()
    print(sorts_types.comb(nums))
    print('Время: ', timeit.default_timer() - start_time)



