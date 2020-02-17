import hashlib

input_string = "ckczppom"
hash_output = hashlib.md5(str.encode(input_string)).hexdigest()[:6]
number = 1
print(hash_output)
while hash_output != "000000":
    hash_output = hashlib.md5(str.encode(input_string + str(number))).hexdigest()[:6]
    number += 1

print(number)