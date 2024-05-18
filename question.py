# mystr = "skibiti1dopdop33"
# alphabets = [char for char in mystr if char.isalpha()]
# print(''.join(alphabets))

# for num in range(2,21,2):
#   print(num)

# for num in range(1, 20, 2):
#    print(num)

# for num in range(10, 0, -1):
#    print(num)

# for num in range(5, 51, 5):
#   print(num)

# for num in range(-1, -11, -1):
#    print(num)

# for num in range(1, 11):
#    doubled_num = num*2
#    print(doubled_num)

# number = int(input("Enter number:"))
# print("the first 10 multiples of", number, "are:")
# for i in range(1, 11):
#     print(number*i)

# for num in range(20, 0, -1):
#     if num % 3 == 0:
#         print(num)

import random

cities = ["paris","london","berlin","tokyo","moscow","beijing","dubai"]

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def provide_hint(city, attempts):
    if attempts == 5:
        return f"Hint: city starts with '{city[0]}'."
    elif attempts == 10:
        return f"Hint: city ends with '{city[-1]}'."
    elif attempts >= 15:
        return f"Hint: city has {len(city)} letters."
    return ""

def city_scramble_game():
    city = random.choice(cities)
    scrambled_city = scramble_word(city)
    attempts = 0

    print("Welcome to Scramble City")
    print(f"Guess the city: {scrambled_city}")

    while True:
        guess = input("Your guess: ").strip()
        attempts += 1

        if guess.lower() == city.lower():
            print(f"Congratulations, You are correct")
            break
        else:
            print("Incorrect guess, try again")
            hint = provide_hint(city, attempts)
            if hint:
                print(hint)

if __name__ == "__main__":
    city_scramble_game()