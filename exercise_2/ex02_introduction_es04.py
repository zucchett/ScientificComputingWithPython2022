lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def calculate_length_of_keys(list_map):
    return list(map(lambda item: len(item), list_map.keys()))

print(calculate_length_of_keys(lang))
