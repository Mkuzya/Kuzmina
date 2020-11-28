my_list = [3, 1, 4, 5, 5, 22, 13]
new = [el for el in my_list if my_list.count(el)==1]
print(new)