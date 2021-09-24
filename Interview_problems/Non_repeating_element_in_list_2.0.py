""" non repeating numbers 0 and 6, find those numbers """
l = [1, 3, 7, 4, 5, 6, 2, 8, 9, 5, 0, 9, 2, 4, 7, 1, 8, 3]
lenny = len(l)
new_l = []

for el in l:
    current_el = l.count(el)
    if current_el == 1:
        new_l.append(str(el))

print(', '.join(new_l))



