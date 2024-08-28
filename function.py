
# Problem 1: Sum of List
# Write a function that takes a list of integers as input and returns the sum of all the integers
def sum_of_list(list):
    sum = 0
    for list_of_num in list:
        sum += list_of_num
    return sum

# numbers = input()
# list_input = list(map(int, numbers.split(' ')))
# sum = sum_of_list(list_input)
# print(sum)
# Problem 2: Factorial Function
""" একটি function লিখুন যা একটি পূর্ণসংখ্যা ইনপুট নেবে এবং তার factorial রিটার্ন করবে।
(Factorial হল একটি সংখ্যা থেকে ছোট সমস্ত সংখ্যা গুণফল, যেমন: 5! = 5 x 4 x 3 x 2 x 1 = 120)। """
def  factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# number = input()
# fact = factorial(int(number))
# print(fact)
# Problem 3: Prime Number Checker
""" একটি function লিখুন যা একটি পূর্ণসংখ্যা ইনপুট নেবে এবং চেক করবে যে সংখ্যাটি একটি prime number কিনা। 
একটি prime number হল এমন একটি সংখ্যা যা কেবলমাত্র ১ এবং নিজেই দ্বারা বিভাজ্য। """
""" def prime_number(n):
    if n == 1:
        print(f"{n} is a prime number")
    elif n == 2:
        print(f"{n} is a prime number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
            else:
                print(f"{n} is a prime number")
number = input()
prime_number(int(number)) """
#Problem 4: Fibonacci Sequence Generator
""" একটি function লিখুন যা একটি পূর্ণসংখ্যা ইনপুট নেবে এবং Fibonacci sequence 
এর প্রথম Nটি সংখ্যার একটি list রিটার্ন করবে। (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...) """
""" def fibonacci_sequence(n):
    a = 0
    b = 1
    fibonacci_list = []
    if n == 1:
        # print(a)
        fibonacci_list.append(a)
    else:
        # print(a)
        fibonacci_list.append(a)
        # print(b)
        fibonacci_list.append(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            # print(c)
            fibonacci_list.append(c)
    return fibonacci_list
n = int(input())
# fibonacci_sequence(int(n))
fibonacci = fibonacci_sequence(n)
print(fibonacci) """
#Problem 5: Palindrome Checker
""" একটি function লিখুন যা একটি string ইনপুট নেবে এবং চেক করবে যে string টি palindrome কিনা। 
একটি palindrome হল এমন একটি শব্দ যা উল্টো করে পড়লেও একই থাকে (যেমন: "radar", "level")। """

""" def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
# s = input()
# print(palindrome(s))
def palinDrome(s):
    b = list(s)
    print(b)
    reverse_b = list(b)
    # print(b.reversec)
    print(reverse_b)
    reverse_b.reverse()
    print(reverse_b)
    if b == reverse_b:
        print(s, "is palindrome")
    else:
        print(s,"is not palindrome")

# s = input()
# palinDrome(s)
# s = input()
# print(s)
# b = s[::-1]
# print(b) """
# Problem 6: Count Vowels in a String
""" একটি function লিখুন যা একটি string ইনপুট নেবে এবং 
সেই string এ কতটি vowel (a, e, i, o, u) আছে তা গণনা করবে। """
""" def count_vowel(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count
s = input()
string_of_count_vowel = count_vowel(s)
print(string_of_count_vowel) """
# Problem 7: Find Maximum of Three Numbers
""" একটি function লিখুন যা তিনটি সংখ্যা ইনপুট নেবে এবং 
তিনটির মধ্যে কোনটি সবচেয়ে বড় তা রিটার্ন করবে। """
""" def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a = int(input())
b = int(input())
c = int(input())
print(max_of_three(a, b, c))
 """
# Problem 8: Convert Celsius to Fahrenheit
""" একটি function লিখুন যা একটি তাপমাত্রা সেলসিয়াসে ইনপুট নেবে এবং 
সেটিকে ফারেনহাইটে রূপান্তর করবে। """
""" def cel_to_fah(c):
    f = (c * 9/5) +32
    return f
c = int(input())
print(cel_to_fah(c)) """
# Problem 9: Find the GCD of Two Numbers
""" একটি function লিখুন যা দুটি পূর্ণসংখ্যা ইনপুট নেবে এবং 
তাদের GCD (Greatest Common Divisor) রিটার্ন করবে। """
""" def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input())
b = int(input())
print(gcd(a, b)) """
# Problem 12: Check if a Number is Armstrong Number
""" একটি function লিখুন যা একটি সংখ্যা ইনপুট নেবে এবং চেক করবে যে 
সংখ্যাটি একটি Armstrong number কিনা। (Armstrong number হল এমন একটি সংখ্যা যা তার 
digitগুলোর cube এর যোগফল তার সমান হয়, যেমন 153 = 1³ + 5³ + 3³)। """
""" def armstrong(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i) ** 3
    if sum == int(n):
        return True
    else:
        return False
n = int(input())
print(armstrong(n)) """
