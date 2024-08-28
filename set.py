
# Problem 1: Set Union and Intersection
""" দুটি set ইনপুট নেয়া হবে এবং প্রোগ্রামটি তাদের union এবং intersection বের করে আউটপুট করবে। """
""" set1_input = input()
set2_input = input()
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
print(union_set)
print(intersection_set) """
# Problem 2: Unique Elements
""" একটি প্রোগ্রাম লিখুন যেখানে একটি list ইনপুট নেয়া হবে এবং
সেই list এর সমস্ত unique উপাদান একটি set এ সংরক্ষণ করা হবে। """
""" list_input = input()
list_value = list(map(int, list_input.split()))
uniqe_list = set(list_value)
print(uniqe_list) """
# Problem 3: Set Difference
""" দুটি set ইনপুট নেয়া হবে এবং প্রোগ্রামটি দেখাবে কোন উপাদানগুলি প্রথম set এ আছে কিন্তু দ্বিতীয় set এ নেই। """
""" set1_input = input()
set2_input = input()
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
set_difference = set1.difference(set2)
print(set_difference) """
# Problem 4: Subset and Superset
""" দুটি set ইনপুট নেয়া হবে এবং প্রোগ্রামটি চেক করবে যে একটি set অন্যটি এর subset বা superset কিনা। """
set1_input = input()
set2_input = input()
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)
if is_subset:
    print("The first set is a subset of the second set.")
else:
    print("The first set is not a subset of the second set.")

if is_superset:
    print("The first set is a superset of the second set.")
else:
    print("The first set is not a superset of the second set.")
