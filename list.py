# Problem 1: Removing Duplicates
""" একটি প্রোগ্রাম লিখুন যেখানে একটি list ইনপুট নেয়া হবে এবং সেই 
list থেকে duplicate (প্রতিলিপি) আইটেমগুলো মুছে ফেলে একটি নতুন list তৈরি করা হবে। """

# numbers = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
""" numbers = input()
numbers_list = list(map(int,numbers.split(',')))
new_numbers = []
for number in numbers_list:
    if number not in new_numbers:
        new_numbers.append(number)
print(new_numbers)
 """
# Problem 2: List Sorting
""" একটি প্রোগ্রাম লিখুন যেখানে একটি list ইনপুট নেয়া হবে এবং 
সেই list টি ascending এবং descending উভয়ভাবে sort করে দেখানো হবে। """
""" numbers = input()
numbers_list = list(map(int, numbers.split(',')))
print(numbers_list)

numbers_list.sort()
print(numbers_list)
numbers_list.sort(reverse=True)
print(numbers_list) """
# Problem 3: List Element Count
""" একটি প্রোগ্রাম লিখুন যেখানে একটি list এর মধ্যে প্রতিটি উপাদান কতবার আছে তা গুণে দেখানো হবে।
যেমন [1, 2, 2, 3, 4, 4, 4] এর জন্য আউটপুট হবে {1: 1, 2: 2, 3: 1, 4: 3}।

 """
""" numbers = input()
numbers_list = list(map(int, numbers.split(',')))
numbers_dic = {}
for number in numbers_list:
    if number in numbers_dic:
        numbers_dic[number] += 1
    else:
        numbers_dic[number] = 1
print(numbers_dic) """
# Problem 4: List Comprehension
""" একটি প্রোগ্রাম লিখুন যা ১ থেকে ১০০ পর্যন্ত সমস্ত সংখ্যা থেকে বর্গ সংখ্যা (square) এর একটি list তৈরি করবে, 
কিন্তু শুধুমাত্র সেই সংখ্যা যেগুলো ৫ দ্বারা বিভাজ্য।
 """
""" square_numbers = [i**2 for i in range(1, 101) if i % 5 == 0]
print(square_numbers) """
# Problem 5: List Indexing
""" একটি প্রোগ্রাম
লিখুন যা ১ থেকে ১০০ পর্যন্ত সংখ্যা থেকে বর্গ সংখ্যা (square) এর একটি list তৈরি করবে,কিন্তু শুধুমাত
দ্বারা বাকি বাকি প্রতিটি সংখ্যা এর একটি সংখ্যা বের করতে হবে।
"""
""" numbers = input()
numbers_list = list(map(int, numbers.split(',')))
square_numbers = [i**2 for i in numbers_list]
print(square_numbers) """
