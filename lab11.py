
def calculate_character_frequency(sentence):
    frequency = {}

    for char in sentence:

        if char != ' ':

            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
                
    return frequency


user_input = input("Please enter a sentence: ")

char_frequency = calculate_character_frequency(user_input)


print("Character frequency in the sentence:")
for char, count in char_frequency.items():
    print(f"'{char}': {count}")
