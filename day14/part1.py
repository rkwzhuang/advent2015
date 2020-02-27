input_string = 2503
# input_string = 1000

comet_distance = 0
dancer_distance = 0

comet_time = 0
dancer_time = 0

while comet_time < input_string:
    comet_distance += 1
    comet_time += (10 + 127)


while dancer_time < input_string:
    dancer_distance += 1
    dancer_time += (11 + 162)

print(comet_distance * 14 * 10)
print(dancer_distance * 16 * 11)