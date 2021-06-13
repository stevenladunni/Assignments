#to run this script type python assignment_4.py
# I first created this script using 2 variables; "current_longest_name" and "names_list".
# then replaced each name in the variable "name_list" with input "name"
# After that, I had the script compare the names in "name_list" which was now called "names" with the variable "current_longest_name" to find which had the most letters.
# If they had the same amount of letter. the program would keep longest of the previous comparison but if the latter was the longest, it would be replacing the previous.
# This was then looped until it had gone through all the names "names_list" and the one that was left standing was selected because it was the longest.
current_longest_name = ""
names_list = ["bob", "jimmy", "max b", "bernie", "jordan","future hendrix"]
for name in names_list:
    if len(name)>len(current_longest_name):
        current_longest_name = name
    else:
        continue
print(current_longest_name)
