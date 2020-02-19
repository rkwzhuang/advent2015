input_string = r'''""
"abc"
"aaa\"aaa"
"\x27"'''

strings = input_string.split("\n")

for string in strings:
    print(len(string), end=" ")
    print("{}".format(string.replace("\"", "")).encode('utf-8').decode('latin-1'), end=" ")
    print(len("{}".format(string.replace("\"", ""))))