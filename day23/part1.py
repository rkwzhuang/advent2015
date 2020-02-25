input_string = """jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""

commands = input_string.split("\n")

instruction_pointer = 0
register_a = 1
register_b = 0

while True:
    try:
        instruction = commands[instruction_pointer][:3]
        parameters = commands[instruction_pointer][4:]
        # print("|" + parameters + "|")

        if instruction == "hlf":
            if parameters == "a":
                register_a /= 2
            else:
                register_b /= 2
        elif instruction == "tpl":
            if parameters == "a":
                register_a *= 3
            else:
                register_b *= 3
        elif instruction == "inc":
            if parameters == "a":
                register_a += 1
                print(register_a)
            else:
                register_b += 1

            print(parameters, register_a, register_b)
            

        if instruction == "jmp":
            if parameters[0] == '-':
                instruction_pointer -= int(parameters[1:])
            else:
                instruction_pointer += int(parameters[1:])
        elif instruction == "jie":
            split_parameters = parameters.split(", ")
            register = split_parameters[0]
            jump_value = split_parameters[1]

            if register == "a":
                if register_a % 2 != 0:
                    instruction_pointer += 1
                    continue
            else:
                if register_b % 2 != 0:
                    instruction_pointer += 1
                    continue

            if jump_value[0] == '-':
                instruction_pointer -= int(jump_value[1:])
            else:
                instruction_pointer += int(jump_value[1:])
        elif instruction == "jio":
            split_parameters = parameters.split(", ")
            register = split_parameters[0]
            jump_value = split_parameters[1]

            if register == "a":
                if register_a != 1:
                    instruction_pointer += 1
                    continue
            else:
                if register_b != 1:
                    instruction_pointer += 1
                    continue

            if jump_value[0] == '-':
                instruction_pointer -= int(jump_value[1:])
            else:
                instruction_pointer += int(jump_value[1:])
        else:
            instruction_pointer += 1

        print(register_a, register_b)

    except IndexError:
        print(register_a, register_b)        
        break


