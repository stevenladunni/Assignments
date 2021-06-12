# To run this script type python assignment_5.py
# Here we are reusing the variables "names_list" and "current_longest_names" from the last assignment but this time, we are defining a function that can be reused over and over for many different arguements or lists.
names_list = ["bob", "jimmy", "max b", "bernie", "jordan","future hendrix"]
def big_name(names):
    current_longest_name = ""
    for name in names:
        if len(name)>len(current_longest_name):
            current_longest_name = name
        else:
            continue
    return current_longest_name
big_name = big_name(names_list)
print(big_name)