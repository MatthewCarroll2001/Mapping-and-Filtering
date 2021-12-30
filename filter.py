
'''
    Filter through a set of numbers using a helper function
'''

#   Number list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#   Find even state function
def find_even(num):
    return num % 2 == 0

#   Filter number list and print results
even_nums = list(filter(find_even, num_list))

print(f'\nList of numbers: {num_list}')
print(f'Even numbers: {even_nums}')

'''
    Can also be used to filter values by type
'''

#   Item list
item_list = ['word', 4, 7.8, 5, 'more words', 9.3]

#   Find strings
def find_words(item):
    return isinstance(item, str)

#   Find numbers
def find_number(item):
    return isinstance(item, int) or isinstance(item, float)

#   Filter item list and print results
words = list(filter(find_words, item_list))
numbers = list(filter(find_number, item_list))

print(f'\nList of items: {item_list}')
print(f'Words: {words}')
print(f'Numbers: {numbers}')