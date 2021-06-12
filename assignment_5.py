# To run this script type python assignment_5.py
names_list = ["bob", "jimmy", "max b", "bernie", "jordan","future hendrix"]
def big_name(names):
    current_longest_name = ""
    for name in names_list:
        if len(name)>len(current_longest_name):
            current_longest_name = name
        else:
            continue
    return current_longest_name
big_name = big_name(names_list)
print(big_name)