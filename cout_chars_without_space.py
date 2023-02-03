def count_chars_without_spaces(input_string):
    return len(input_string.replace(" ", ""))

input_string = input("Inserisci una stringa: ")
print("Il numero di caratteri senza spazi è: ", count_chars_without_spaces(input_string))
input("press enter to exit")
