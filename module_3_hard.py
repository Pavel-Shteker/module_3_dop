def calculate_structure_sum(data_structure):
    total = 0

    def sum99(step):
        nonlocal total
        if isinstance(step, int):  # чек на число
            total += step
        elif isinstance(step, str):  # чек на строку
            total += len(step)
        elif isinstance(step, list):  # чек на список
            for sub_item in step:
                sum99(sub_item)
        elif isinstance(step, dict):  # чек на словарь
            for keys, loot in step.items():
                sum99(keys)
                sum99(loot)
        elif isinstance(step, tuple):  # чек на кортеж
            for sub_item in step:
                sum99(sub_item)
        elif isinstance(step, set):  # чек на множество
            for sub_item in step:
                sum99(sub_item)
# итого пять структур

    for checking in data_structure:
        sum99(checking)
    return total

# абракадабра
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

resulting_sum = calculate_structure_sum(data_structure)
print(resulting_sum)