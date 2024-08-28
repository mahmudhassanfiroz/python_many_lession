
# Problem 1: Frequency Counter
""" একটি প্রোগ্রাম লিখুন যেখানে একটি string ইনপুট নেয়া হবে এবং 
সেই string এর প্রতিটি character এর frequency (প্রতিটি character কতবার এসেছে)
একটি dictionary তে গণনা করে দেখানো হবে। """
""" char_freq = input()
char_dic = {}
for char in char_freq:
    if char in char_dic:
        char_dic[char] += 1
    else:
        char_dic[char] = 1
print(char_dic) """
#Problem 2: Student Grades
""" একটি dictionary ইনপুট নেয়া হবে যেখানে শিক্ষার্থীদের নাম এবং তাদের প্রাপ্ত নম্বর থাকবে। 
প্রোগ্রামটি সেই dictionary থেকে সর্বোচ্চ এবং সর্বনিম্ন নম্বর পাওয়া শিক্ষার্থীদের নাম এবং নম্বর প্রিন্ট করবে। """
""" student_grades = {}
while True:
    name = input()
    if name == '':
        break
    grade = int(input())
    student_grades[name] = grade 
    print(student_grades)
max_student_grade = max(student_grades, key=student_grades.get)
min_student_grade = min(student_grades, key=student_grades.get)
print(max_student_grade,{student_grades[max_student_grade]}, min_student_grade, {student_grades[min_student_grade]})
 """
# Problem 3: Dictionary Merging
""" দুটি dictionary ইনপুট নেয়া হবে এবং সেগুলি merge করে একটি নতুন dictionary তৈরি করা হবে।
যদি কোনো key উভয় dictionary তেই থাকে, তাহলে পরবর্তী dictionary এর value প্রাধান্য পাবে। """
""" dict1 = {}
dict2 = {}
while True:
    key = input()
    if key == '':
        break
    value = int(input())
    dict1[key] = value 
while True:
    key = input()
    if key == '':
        break
    value = int(input())
    dict2[key] = value
dict3 = {**dict1, **dict2}
print(dict3) """
# Problem 4: Inverted Dictionary
""" একটি dictionary ইনপুট নেয়া হবে যেখানে keys এবং values থাকবে। 
প্রোগ্রামটি একটি নতুন dictionary তৈরি করবে যেখানে keys এবং values গুলো উল্টো করে দেয়া হবে। """
original_dict = {}
while True:
    key = input()
    if key == '':
        break
    value = int(input())
    original_dict[key] = value
inverted_dict = {}
for key, value in original_dict.items():
    if value in inverted_dict:
        inverted_dict[value].append(key)
    else:
        inverted_dict[value] = [key]
print(inverted_dict) 

