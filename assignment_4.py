

current_longest_name = ""
names_list = ["bob", "jimmy", "max b", "bernie", "jordan","future hendrix"]
for name in names_list:
    if len(name)>len(current_longest_name):
        current_longest_name = name
    else:
        continue
print(current_longest_name)
