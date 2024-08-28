
# SHA-256 
# initial shash text 
import hashlib
import os


text = 'Hello, World!'
# # encode text to bytes
# text_bytes = text.encode('utf-8')
# # create a new SHA-256 hash object
# hash_object = hashlib.sha256()
# # update hash object with text bytes
# hash_object.update(text_bytes)
# # get the hexadecimal representation of the hash
# hash_hex = hash_object.hexdigest()
# print(hash_hex)
# একটি SHA-256 হ্যাশ অবজেক্ট তৈরি করা
hash_object = hashlib.sha256()
# টেক্সটটি এনকোড করে হ্যাশ অবজেক্টে আপডেট করা
hash_object.update(text.encode('utf-8'))
# হ্যাশের হেক্সাডেসিমাল রূপ  পাওয়া
hash_hex = hash_object.hexdigest()
# print(hash_hex)

# একটি MD5 হ্যাশ অবজেক্ট তৈরি করা
md5_hash = hashlib.md5()
# টেক্সটটি িএনকোড করে হ্যাশ অবজেক্টে আপডেট করা
md5_hash.update(text.encode('utf-8'))
# হ্যাশের হেক্সাডেসিমাল রূপ পাওয়া
md5_hex = md5_hash.hexdigest()
# print(f'MD5 hash: {md5_hex}')
# SHA-1
sha1_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
# SHA-512
sha512_hash = hashlib.sha512(text.encode('utf-8')).hexdigest()
# SHA-3-256
sha3_256_hash = hashlib.sha3_256(text.encode('utf-8')).hexdigest()
# print(f'SHA-1 Hash : {sha1_hash}')
# print(f'SHA-512 Hash : {sha512_hash}')
# print(f'SHA-3-256 Hash : {sha3_256_hash}')
# আসল টেক্সট 
original_text = 'Hello, World!'
# আসল টেক্সটটি হ্যাশ করা 
original_hash = hashlib.sha256(original_text.encode('utf-8')).hexdigest()
# টেক্সটি প্রাপ্তি এবং হ্যাশ করা 
received_text = 'Hello, World!'
received_hash = hashlib.sha256(received_text.encode('utf-8')).hexdigest()
# হ্যাশগুলি তুলনা করা 
# if original_hash == received_hash:
#     print('Correct data')
# else:
#     print('Incorrect data')
# একটি র‌্যান্ডম সল্ট তৈরি করা 
salt = os.urandom(16) # 16 bytes of random data
# সল্টের সাথে টেক্সট যোগ করা 
salted_text = text.encode('utf-8') + salt 
# সল্টেড টেক্সটটি হ্যাশ করা 
salted_hash = hashlib.sha256(salted_text).hexdigest()
print(f'salt : {salt.hex()}')
print(f'salted SHA-256 Hash : {salted_text}')

