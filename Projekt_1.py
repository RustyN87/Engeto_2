"""
projekt_1.py: první projekt do Engeto online Python Akademie

author: Radim Novotný
email: r.novotny@centrum.cz
"""
print(50 * "=")
print(
    """              Welcome to the app

     Please enter your username and password   
         """)
print(50 * "=")

import re

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

def authenticate_user():
    print()
    username = input("username:")
    print(15 * "=")
    password = input("password:")
    print(15 * "=")

    if username in registered_users and registered_users[username] == password:
        print(f"Welcome to the app, {username}")

    else:  
        print("unregistered user, terminating the program...")
        exit()

if __name__ == "__main__":

    authenticate_user()

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

def count_words(text):
    words = text.split()
    return len(words)

def count_capitalized_words(text):
    words = text.split()
    capitalized_count = 0
    for word in words:
            if word[0].isupper():
                capitalized_count += 1
    return capitalized_count

def count_uppercase_words(text):
    words = text.split()
    uppercase_count = 0
    for word in words:
        if word.isupper():
            uppercase_count += 1
    return uppercase_count

def count_lowercase_words(text):
    words = text.split()
    lowercase_count = 0
    for word in words:
        if word.islower():
            lowercase_count += 1
    return lowercase_count

def count_numbers(text):
    numbers = re.findall(r"\b\d+\b",text)
    return len(numbers)

def sum_numbers(text):
    numbers = re.findall(r"\b\d+\b",text)
    return sum(map(int,numbers))

def word_length_frequencies(text):
    length_frequencies = {}
    words = text.split()
    for word in words:
        clean_word = word.strip(".,!?;:()").lower()
        if clean_word:
            length = len(clean_word)
            length_frequencies[length] = length_frequencies.get(length, 0) + 1
    return length_frequencies

def print_word_length_graph(length_frequencies):
    max_length = max(length_frequencies.keys(), default=0)
    print("+", "-" * 26, "+")
    print(f"| {'LEN':<3}|{'OCCURRENCES':^17}|{'NR.':>4} |")
    print("+", "-" * 26, "+")
    for i in range(1, max_length + 1):
        graph = "*" * length_frequencies.get(i, 0)
        print(f"| {i:<3}|{graph:<17}|{length_frequencies.get(i, 0):>4} |")
    print("+", "-" * 26, "+")

def main():
   
    print("We have 3 texts to be analyzed.")
    print(31 * "=")

    try:
        user_choice = int(input("Enter a number btw. 1 and 3 to select: "))
        print(40 * "=")
        if 1 <= user_choice <= len(TEXTS):
            selected_text = TEXTS[user_choice - 1]
            word_count = count_words(selected_text)
            print(f"There are {word_count} words in the selected text.")
            capitalized_count = count_capitalized_words(selected_text)
            print(f"There are {capitalized_count} titlecase words.")
            uppercase_count = count_uppercase_words(selected_text)
            print(f"There are {uppercase_count} uppercase words.")
            lowercase_count = count_lowercase_words(selected_text)
            print(f"There are {lowercase_count} lowercase words.")
            numbers_count = count_numbers(selected_text)
            print(f"There are {numbers_count} numeric strings.")
            numbers_sum = sum_numbers(selected_text)
            print(f"The sum of all the numbers {numbers_sum}")
            print(40 * "=")

            length_frequencies = word_length_frequencies(selected_text)
            print_word_length_graph(length_frequencies)
         
        else:
            print("Error: The entered number is not in the menu. terminating the program.")
            return
    except ValueError:
        print("Error : The input provide is not a number. terminating the program.")
        return
    
if __name__ == "__main__":

 main()