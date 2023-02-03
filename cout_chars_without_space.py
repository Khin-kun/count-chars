def count_chars_without_spaces(input_string):
    return len(input_string.replace(" ", ""))

input_string = input("Enter a string: ")
print("The number of characters without spaces is: ", count_chars_without_spaces(input_string))
input("press enter to exit")
