# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open('./Input/Names/invited_names.txt') as f:
    names = f.readlines()
for name in names:
    #print(name.strip())
    with open('./Input/Letters/starting_letter.txt') as f:
        letter_content = f.read()
    letter_content = letter_content.replace('[name]', name.strip()) # use PLACEHODER strriped name amkes the code cleaner

    with open(f'./Output/ReadyToSend/letter_to_{name}.txt', 'w') as f:
        f.write(letter_content)
