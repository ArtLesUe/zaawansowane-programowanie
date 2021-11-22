def two_lists_merge_deduplicate_and_cubing(list_a: list, list_b: list) -> list:
    list_c = list_a + list_b
    list_c = list(dict.fromkeys(list_c))
    return [val * val * val for val in list_c]


list_a = list()
list_a.append(1)
list_a.append(2)
list_a.append(3)
list_a.append(4)
list_a.append(5)

list_b = list()
list_b.append(4)
list_b.append(5)
list_b.append(6)
list_b.append(7)
list_a.append(8)
list_a.append(9)

print(two_lists_merge_deduplicate_and_cubing(list_a, list_b))
