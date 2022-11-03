lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def calculate_keys_length(list_map):
    return list(map(lambda item: len(item), list_map.keys()))
print("keys length:",calculate_keys_length(lang))