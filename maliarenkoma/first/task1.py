"""
Порахувати кількість пустих списків
"""
l = [1, 2, [], [1, 2], [], []]

i = 0
num_of_empty_lists = 0
while i < len(l):
    if isinstance(l[i], list) and len(l[i]) == 0:
        num_of_empty_lists += 1
    i += 1

print(num_of_empty_lists)
