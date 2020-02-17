import hashlib

input_string = "ckczppom"
hash_output = hashlib.md5(str.encode(input_string)).hexdigest()[:5]
number = 1
print(hash_output)
while hash_output != "00000":
    hash_output = hashlib.md5(str.encode(input_string + str(number))).hexdigest()[:5]
    number += 1

print(number)