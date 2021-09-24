""" repeating number 0, find it """
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
lenny = len(l)
new_l = []

for el in l:
    current_el = l.count(el)
    if current_el == 2:
        new_l.append(el)
        break
print(*new_l)
