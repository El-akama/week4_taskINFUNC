# from functools import reduce

# task1
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = list(map(lambda x: x**2, some_list))
# print(new_list)

# task2 
# enter = list(input("введите числа: "))
# news = [int(x) for x in enter]
# print(sum(news))

# task3 
# nums = [1, 2, 3, 0, -1]
# print(nums)
# print(all(nums))

# task4
# nums = [1, 2, 3, 0, -1]
# print(nums)
# print(any(nums))

# task5
# nums = [1, 2, 3, 0, -1]
# negative = list(filter(lambda x: x < 0, nums))
# print(negative)

# task6
# nums = [1, 2, 3, 0, -1, 4, 6]
# chet = list(filter(lambda x: x % 2 == 0, nums))
# print(chet)

# task7
# slova = ['hello', 'world', 'incapsulation', 'inheritance']
# dlina = list(filter(lambda x: len(x) > 6, slova))
# print(dlina)

# task8
# nums = [1, 2, 3, 4, 5, 6]
# umnoj = reduce(lambda a, b: a * b, nums)
# print(umnoj)

# task9
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums1 = len(list(filter(lambda a: a % 2 == 0, nums)))
# nums2 = len(list(filter(lambda a: a % 2, nums)))
# print(f"количество четных чисел {nums1}")
# print(f"количество не четных чисел {nums2}")

# task10
# nums = [-2, 4, -3, 6, -5, 8]
# num_odd = list(map(lambda even: even, filter(lambda x: x < 0, nums)))
# num_even = list(map(lambda odd: odd, filter(lambda x: x >= 0, nums)))
# print(f'Не чётный:{num_odd}\nЧётный:{num_even}')

# task11
# def numbers(num):
#     if num > 0:
#         return 1
#     elif num < 0:
#         return -1
#     else: 
#         return 0 
# nums = [-1, 2, 3, 4, -5, 6, 7, -8, 9, 0]
# new_num = list(map(numbers, nums))
# print(new_num)

# task12
# some_list = list(input("введите список из чисел: "))
# some_step = int(input("введите шаг: "))
# some_step %= len(some_list)
# new_list = list(some_list[some_step:] + some_list[:some_step])
# print(new_list)

# task13
# srez = int(input("введите число среза: "))
# mass = [x for x in input("введите числа через пробел: ").split()]
# for i in range(srez):
#     print(mass[srez-1-i], end = " ")

# # хз какой из них правильный (почему то не работает в хакерранке)

# n = int(input("введите число среза: "))
# array = input("введите числа через пробел: ").split()
# def reversed(array):
    
#     some_str = ""
#     for i in range(n):
#         some_str += array[n-1-i] + " "
        
#     print(some_str.strip())

# reversed(array)


# task14

# # def balans(lit):
# #     if lit == ')':
# #         return '('
# #     elif lit == '}':
# #         return '{'
# #     elif lit == ']':
# #         return '['

# num = int(input("введите число: "))
# for x in range(num):
#     literals = input("введите литералы: ").strip()
#     flag = 1
#     new_list = []
#     for lit in literals:
#         if lit in ['{','[','(']:
#             new_list.append(lit)
#         elif new_list and new_list.pop() == lit:
#             flag = 0
#             break
#     if len(new_list) == 0:
#         print("yes")
#     else:
#         print("no")