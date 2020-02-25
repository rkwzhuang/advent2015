input_string = "abcddee"

# 97-122
string_list = list(map(lambda x: ord(x), input_string))

print(string_list)
def check_first_requirement(password):
    for i in range(0, len(password) - 2):
        if (password[i + 2] - password[i] - password[i + 1]):
            return True

    return False

def check_second_requirement(password):
    if 105 in password or 111 in password:
        return False
    else:
        return True

def check_third_requirement(password):
    index = 0
    num_pairs = 0
    while index < len(password):
        if password[index] == password[index]:
            num_pairs += 1
            index += 2
        else:
            index += 1
    
    if num_pairs >= 2:
        return True
    else:
        return False

print(check_first_requirement(string_list))
print(check_second_requirement(string_list))
print(check_third_requirement(string_list))

digit = -1
while string_list != [97, 98, 99, 100, 101, 102, 122, 122]:
    string_list[digit] += 1
    if string_list[digit] == 123:
        string_list[digit] = 97
        digit -= 1
        print(digit)
    print(string_list)

    # break