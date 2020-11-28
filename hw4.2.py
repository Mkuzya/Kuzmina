my_list = [5, 10, 7, 3, 1, 6, 13, 4, 17]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)