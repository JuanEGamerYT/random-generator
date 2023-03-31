import itertools
import random
import os

# Ask if special characters will be included
special_characters = input("Do you want to include special characters? (y/n): ")

if special_characters.lower() == "y":
    # Define the characters to be combined, including special characters
    characters = "abcdefghijklmnopqrstuvwxyz!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    characters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
else:
    # Define the characters to be combined, without special characters
    characters = "abcdefghijklmnopqrstuvwxyz"
    characters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

# Ask for the amount of uppercase and lowercase letters to include
upper_count = int(input("Enter the number of uppercase letters you want to include: "))
lower_count = int(input("Enter the number of lowercase letters you want to include: "))

# Ask for the amount of numbers to include
number_count = int(input("Enter the number of numbers you want to include: "))

# Ask for the number of combinations to generate
combination_count = int(input("Enter the number of combinations you want to generate: "))

# Calculate the total length of each combination
length = upper_count + lower_count + number_count

# Create a "Generated" directory in the parent directory
dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
generated_dir = os.path.join(dir_path, "Generated")
os.makedirs(generated_dir, exist_ok=True)

# Generate multiple combinations
for i in range(combination_count):
    # Choose characters to use in each combination
    characters_list = [random.choice(characters) for i in range(length-upper_count-lower_count-number_count)]
    characters_upper_list = [random.choice(characters_upper) for i in range(upper_count)]
    characters_lower_list = [random.choice(characters) for i in range(lower_count)]
    numbers_list = [random.choice(numbers) for i in range(number_count)]

    # Combine all the characters
    characters_list.extend(characters_upper_list)
    characters_list.extend(characters_lower_list)
    characters_list.extend(numbers_list)

    # Shuffle the characters to generate unique combinations
    random.shuffle(characters_list)

    # Convert the list of characters to a string
    combination = ''.join(characters_list)

    # Write the combination to the "generated.txt" file in the "Generated" directory
    file_path = os.path.join(generated_dir, "generated.txt")
    with open(file_path, "a") as file:
        file.write(combination + "\n")

print(f"{combination_count} combinations have been generated in the 'generated.txt' file in the 'Generated' directory.")
