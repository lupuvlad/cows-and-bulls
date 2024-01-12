import random


# This method replace the @new_character, in @original_string, at position @pos
def get_replace_string_character_at(pos, new_character, original_string):
    string_list = list(original_string)
    string_list[pos] = new_character

    return ''.join(string_list)


# Generates a random number between 1000 and 9999 and convert it as a string
def generate_initial_number():
    return str(random.randint(1000, 9999))


# Generates a random digit between 0 and 9 and convert it as a string
def generate_new_digit():
    return str(random.randint(0, 9))


# Checks if there are repeated digits
def is_digit_repeated(digit, number):
    return number.count(str(digit)) > 1


# Checks if the first digit is not zero
def is_digit_valid(string_number):
    if int(string_number[0]) == 0:
        return False
    return True


# This method should return a digit that is unique in the parameter number
def get_unique_digit(i, number):
    copy_of_number = number

    if not is_digit_repeated(copy_of_number[i], copy_of_number) and is_digit_valid(copy_of_number):
        return copy_of_number[i]

    new_digit = copy_of_number[i]

    while is_digit_repeated(new_digit, copy_of_number) or not is_digit_valid(copy_of_number):
        new_digit = generate_new_digit()

        copy_of_number = get_replace_string_character_at(i, new_digit, copy_of_number)

    return new_digit


# This method will return the final number, with each digit unique.
def get_final_generated_number(initial_generated_number):
    final_generated_number = initial_generated_number

    for i in range(len(final_generated_number)):
        final_generated_number = get_replace_string_character_at(i, get_unique_digit(i, final_generated_number),
                                                                 final_generated_number)

    return final_generated_number


def generate_different_digit_number():
    initial_generated_number = generate_initial_number()

    return get_final_generated_number(initial_generated_number)


# Input for the guess
def guess_the_number(msg):
    return input(msg)


# Checks if the guessed number has exactly 4 digits
def is_4digit_number(number):
    return len(number) == 4


# Checks if the guessed number has repeated digits
def has_number_repeated_digits(number):
    for digit in number:
        if is_digit_repeated(digit, number):
            return True
    return False


# Checks if the guessed number is valid
def is_guessed_number_valid(number):
    return not has_number_repeated_digits(number) and is_4digit_number(number) and is_digit_valid(number)


# Checks if the number is not valid and tells you to write another one
def user_guessed_number(msg):
    user_number = guess_the_number(msg)

    while not is_guessed_number_valid(user_number):
        user_number = guess_the_number("Number not valid. Guess again: ")

    return user_number


# Checks if the guessed number is the same with the computer's generated number
def numbers_are_the_same(gen_number, guess_number):
    return gen_number == guess_number


# Calculate the number of cows
def calculate_cows(gen_number, guess_number):
    cows = 0
    for i in range(len(guess_number)):
        if guess_number[i] in gen_number and not guess_number[i] == gen_number[i]:
            cows += 1
    return cows


# Calculate the number of bulls
def calculate_bulls(gen_number, guess_number):
    bulls = 0
    for i in range(len(guess_number)):
        if guess_number[i] == gen_number[i]:
            bulls += 1
    return bulls


# Main function
def main():
    count = 1
    generated_number = generate_different_digit_number()
    # print(generated_number)
    user_final_number = user_guessed_number("Guess the 4-digit number: ")
    cows = calculate_cows(generated_number, user_final_number)
    bulls = calculate_bulls(generated_number, user_final_number)
    while not numbers_are_the_same(generated_number, user_final_number):
        count += 1
        print(f"{cows} cows and {bulls} bulls")
        user_final_number = user_guessed_number("Wrong number! Guess again: ")
        cows = calculate_cows(generated_number, user_final_number)
        bulls = calculate_bulls(generated_number, user_final_number)

    print(f"Congratulations! You've guessed the number in {count} guesses.")


main()
