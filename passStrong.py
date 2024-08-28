# Problem 7: Password Strength Checker
""" import re

password = input()

if len(password) >= 8 and re.search(r'\d', password) and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
    print("Password is strong")
else:
    print("Password is weak")
 """
# Problem 8: FizzBuzz Problem
""" একটি প্রোগ্রাম লিখুন যা ১ থেকে ১০০ পর্যন্ত সংখ্যা প্রিন্ট করবে, তবে:

যদি সংখ্যা ৩ দ্বারা বিভাজ্য হয়, প্রিন্ট করবে "Fizz"
যদি সংখ্যা ৫ দ্বারা বিভাজ্য হয়, প্রিন্ট করবে "Buzz"
যদি সংখ্যা ৩ এবং ৫ উভয় দ্বারা বিভাজ্য হয়, প্রিন্ট করবে "FizzBuzz" """
""" number = int(input())
for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) """
# Problem 9: Age Group Identifier
""" একটি প্রোগ্রাম লিখুন যেখানে একজন ব্যবহারকারী তার বয়স ইনপুট করবে এবং প্রোগ্রামটি সিদ্ধান্ত নেবে সে কোন বয়সের দলে পড়ে:

০-১২ বছর: "Child"
১৩-১৭ বছর: "Teenager"
১৮-৫৯ বছর: "Adult"
৬০ বা তার বেশি: "Senior" """
""" age = int(input())
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 17:
    print("Teenager")
elif age >= 18 and age <= 59:
    print("Adult")
else:
    print("Senior")
 """
# Problem 10: Discount Calculator
""" একটি প্রোগ্রাম লিখুন যেখানে একজন ব্যবহারকারী ক্রয়ের পরিমাণ ইনপুট করবে এবং প্রোগ্রামটি ডিসকাউন্টের পরিমাণ নির্ধারণ করবে:

যদি ক্রয়ের পরিমাণ ১০০০ বা তার বেশি হয়, তাহলে ১০% ডিসকাউন্ট দিন।
যদি ক্রয়ের পরিমাণ ৫০০ থেকে ৯৯৯ এর মধ্যে হয়, তাহলে ৫% ডিসকাউন্ট দিন।
যদি ক্রয়ের পরিমাণ ৫০০ এর কম হয়, তাহলে কোন ডিসকাউন্ট নেই। """
""" sell_price = int(input())
if sell_price >= 1000:
    discount = sell_price * 10/100
    print(discount)
    final_price = sell_price - discount
    print(final_price)
elif sell_price <= 999 and sell_price >= 500:
    discount = sell_price * 5/100
    print(discount)
    final_price = sell_price - discount
    print(final_price)
else:
    print("No Discount for you") """
