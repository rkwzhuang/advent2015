input_string = "1113222113"

for i in range(0,50):
    character_count = 1
    character = 0
    new_string = ""
    while character < len(input_string):
        try:
            current_character = input_string[character]
            next_character = input_string[character+1]
            if current_character == next_character:
                character_count += 1
            else:
                new_string += str(character_count) + str(current_character)
                character_count = 1
        except IndexError:
            new_string += str(character_count) + str(current_character)


        character += 1

    input_string = new_string
        
print(len(new_string))