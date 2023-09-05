def fix_list_wagons(wagon_id, missing_wagons):
    first, second, locomotive, *etc = wagon_id
    return [locomotive, *missing_wagons, *etc, first, second]

result = fix_list_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])

#exppected output: [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]

print(result)