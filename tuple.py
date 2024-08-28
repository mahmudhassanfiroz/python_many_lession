
# Problem 1: Tuple Packing and Unpacking
""" একটি প্রোগ্রাম লিখুন যেখানে তিনটি আলাদা মান (যেমন একটি নাম, বয়স, এবং একটি শহর) ইনপুট নেয়া হবে 
এবং tuple প্যাকিং এবং আনপ্যাকিং ব্যবহার করে সেই মানগুলিকে একটি tuple এ সংরক্ষণ করা এবং 
পুনরুদ্ধার করা হবে। """
""" name = input()
age = int(input())
city = input()
person_info = (name, age, city)
print(person_info)
name_unpace,age_unpace,city_unpace = person_info
print(name_unpace,age_unpace,city_unpace)
 """
# Problem 2: Tuple Immutability
""" একটি প্রোগ্রাম লিখুন যেখানে একটি tuple ইনপুট নেয়া হবে এবং 
আপনি চেষ্টা করবেন tuple এর একটি আইটেম পরিবর্তন করতে। 
এটি চেষ্টা করার পর tuple এর অপরিবর্তনীয়তা (immutability) সম্পর্কে জানতে পারবেন।
"""
""" tuple_input = input()
tuple_values = tuple(map(str.strip, tuple_input.split(',')))
print(tuple_values) """
# Problem 3: Tuple Indexing and Slicing
""" একটি tuple ইনপুট নেয়া হবে এবং tuple থেকে একটি নির্দিষ্ট range বা slice বের করে আউটপুট করা হবে। """
tuple_input = input()
tuple_values = tuple(map(str.strip, tuple_input.split(',')))
print(tuple_values)
start_index = int(input())
end_index = int(input())
tuple_slice = tuple_values[start_index:end_index]
print(tuple_slice)