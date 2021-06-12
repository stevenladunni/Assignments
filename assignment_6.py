# to run this script type python assignment_6.py
names_list = ["bob", "jimmy", "max b", "bernie", "jordan","future hendrix"]

def separate(lst_names):
    even_lst = []
    odd_lst = []

    for name in names_list:
        if len(name) % 2 == 0:  #len is even
            even_lst.append(("b"+name[1:]))
        else:
            odd_lst.append((name[:-1]+"c"))

    print(even_lst)
    print(odd_lst)
    return even_lst

even_list = separate(names_list)
print(even_list)