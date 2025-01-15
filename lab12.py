
def sum_of_dictionary_items(input_dict):
    return sum(input_dict.values())


dict1 = {'a': 100, 'b': 200, 'c': 300}
total_sum1 = sum_of_dictionary_items(dict1)
print("Input:", dict1)
print("Output:", total_sum1)


dict2 = {'x': 25, 'y': 18, 'z': 45}
total_sum2 = sum_of_dictionary_items(dict2)
print("Input:", dict2)
print("Output:", total_sum2)
