import functools

input_string = 33100000
number_to_check = int(input_string ** 0.5)
number_to_check = int(1472600 / 2)

def get_factors(number):
    results = set()
    for i in range(1, int((number ** 0.5)) + 1):
        if number % i == 0:
            results.add(i)
            results.add(int(number/i))
    return results

def get_presents_delivered(house_num):
    elves = list(get_factors(house_num))

    return functools.reduce(lambda x, y: x + y, map(lambda x: x * 10, elves))

# while get_presents_delivered(number_to_check) < input_string:
#     number_to_check += 1
#     print(number_to_check)

# while get_presents_delivered(number_to_check) <= input_string:
#     print(number_to_check)
#     number_to_check -= 1


print("answer", get_presents_delivered(776160))

# 33100000
# 44183040