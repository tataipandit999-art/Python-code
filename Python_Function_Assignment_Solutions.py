# Python Function Assignment Solutions
# Q1 - Q30

# Q1. Check Even or Odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

check_even_odd(68)


# Q2. Check Positive, Negative or Zero
def check_number(n):
    if n < 0:
        print(f"{n} is a negative num")
    elif n > 0:
        print(f"{n} is a positive num")
    else:
        print(f"{n} is 0")

check_number(20)


# Q3. Find Largest of Two Numbers
def find_largest(a, b):
    if a >= b:
        return a
    else:
        return b

print(find_largest(0.9, 1.9))


# Q4. Find Largest of Three Numbers
def find_largest_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(find_largest_three(100, 22, 10))


# Q5. Sum of Natural Numbers
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)

sum_natural(100)


# Q6. Multiplication Table
def multiplication_table(n):
    if n < 1 or n > 10:
        return None

    for i in range(1, 11):
        print(i * n, end=" ")

multiplication_table(1)


# Q7. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))


# Q8. Count Digits
def count_digits(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count

print(count_digits(12345))


# Q9. Reverse Number
def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return reverse

print(reverse_number(12345))


# Q10. Check Prime
def check_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(check_prime(29))


# Q11. Count Characters
def count_characters(text):
    count = 0

    for char in text:
        count += 1

    return count

print(count_characters("Python"))


# Q12. Count Vowels
def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count

print(count_vowels("education"))


# Q13. Count Consonants
def count_consonants(text):
    count = 0

    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1

    return count

print(count_consonants("Python Programming"))


# Q14. Count Vowels and Consonants
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1

    print("Vowels :", vowels)
    print("Consonants :", consonants)

count_vowels_consonants("Python Programming")


# Q15. Reverse String
def reverse_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse

    print("Using loop :", reverse)
    print("Using slicing :", text[::-1])

reverse_string("Python")


# Q16. Check Palindrome
def check_palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome("madam")


# Q17. Count Words
def count_words(text):
    count = 0
    in_word = False

    for char in text:
        if char != " " and not in_word:
            count += 1
            in_word = True
        elif char == " ":
            in_word = False

    return count

print(count_words("Python is easy to learn"))


# Q18. Character Frequency
def character_frequency(text, ch):
    count = 0

    for char in text:
        if char == ch:
            count += 1

    return count

print(character_frequency("programming", "g"))


# Q19. Remove Spaces
def remove_spaces(text):
    result = ""

    for char in text:
        if char != " ":
            result += char

    return result

print(remove_spaces("Python Programming Language"))


# Q20. Convert to Uppercase
def convert_uppercase(text):
    print(text.upper())

    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        else:
            result += char

    print(result)

convert_uppercase("Python Programming")


# Q21. Count Uppercase, Lowercase, Digits and Spaces
def count_case(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            digits += 1
        elif char == " ":
            spaces += 1

    print("Uppercase :", uppercase)
    print("Lowercase :", lowercase)
    print("Digits :", digits)
    print("Spaces :", spaces)

count_case("Python123 ABC")


# Q22. First Character
def first_character(text):
    for char in text:
        print(char)
        break

first_character("PYTHON")


# Q23. Last Character
def last_character(text):
    print(text[-1])

    last = ""
    for char in text:
        last = char

    print(last)

last_character("PYTHON")


# Q24. Display Every Character
def display_characters(text):
    for char in text:
        print(char)

display_characters("PYTHON")


# Q25. Display Character with Position
def display_position(text):
    for i in range(len(text)):
        print("Position", i, ":", text[i])

display_position("JAVA")


# Q26. Remove Vowels
def remove_vowels(text):
    result = ""

    for char in text:
        if char.lower() not in "aeiou":
            result += char

    return result

print(remove_vowels("Python Programming"))


# Q27. Find Longest Word
def find_longest_word(text):
    longest = ""
    current = ""

    for char in text:
        if char != " ":
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = ""

    if len(current) > len(longest):
        longest = current

    return longest

print(find_longest_word("Python Programming Language"))


# Q28. Count Each Vowel Separately
def count_vowels_separately(text):
    a = e = i = o = u = 0

    for char in text.lower():
        if char == "a":
            a += 1
        elif char == "e":
            e += 1
        elif char == "i":
            i += 1
        elif char == "o":
            o += 1
        elif char == "u":
            u += 1

    print("a =", a)
    print("e =", e)
    print("i =", i)
    print("o =", o)
    print("u =", u)

count_vowels_separately("education")


# Q29. Star Pattern
def star_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()

star_pattern(5)


# Q30. Number Pattern
def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

number_pattern(5)
