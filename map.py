'''
    Map functions to lists to iterate through operations efficiently
'''

#   Number list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#   Helper function
def square_number(num):
    return num * num

#   Map function and list
squared_nums = list(map(square_number, num_list))

#   Print results
print(f'\nList of numbers: {num_list}')
print(f'Squared numbers: {squared_nums}')


'''
    Can also be used to map keys with index values to create a map collection (hashing)
'''

#   Basic hashmap class
class Hashmap:

    #   Map implemented as list
    items = []

    def __init__(self):
        for x in range(10):
            #   Each map index contains a list for open hashing(aka separate chaining)
            self.items.append([])

    #   Convert keys to index values
    def hash_function(self, key):
        return key % 10

    #   Append item to map
    def add(self, key, value):
        self.items[value].append(key)

    #   For printing items in map
    def __str__(self):
        string = '\n'
        for item in self.items:
            string += f'{item}\n'
        return string

#   Instantiate map
hashmap = Hashmap()

#   Key list
key_list = [13, 45, 69, 54, 58, 2, 0, 12, 14, 33]

#   Map keys to index values for hashmap and print results
value_list = list(map(hashmap.hash_function, key_list))

for i in range(len(value_list)):
    hashmap.add(key_list[i], value_list[i])

print(f'\nKey values:{key_list}')
print(f'Map using separate chaining (index = key % 10):{hashmap}')