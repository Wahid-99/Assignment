#solutin-1
def is_prime(n):
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime numbers

    # Exclude multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for factors from 5 to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Take input from user
n = int(input("Enter an integer: "))

# Check and output result
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")

#solution-2
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Take input from user
n = int(input("Enter an integer: "))

# Print the multiplication table
print_multiplication_table(n)

#solution-3
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \nEnter 1 or 2: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
else:
    print("Invalid choice.")

#solution-4
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \n3. Check Palindrome \nEnter 1, 2, or 3: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
elif choice == "3":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
else:
    print("Invalid choice.")

#solution-5
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {vowel_count}")

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \n3. Check Palindrome \n4. Count Vowels \nEnter 1, 2, 3, or 4: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
elif choice == "3":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == "4":
    s = input("Enter a string: ")
    count_vowels(s)
else:
    print("Invalid choice.")

#solution-6
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {vowel_count}")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    print(f"GCD of {a} and {b} is: {a}")

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \n3. Check Palindrome \n4. Count Vowels \n5. Find GCD \nEnter 1, 2, 3, 4, or 5: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
elif choice == "3":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == "4":
    s = input("Enter a string: ")
    count_vowels(s)
elif choice == "5":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    find_gcd(a, b)
else:
    print("Invalid choice.")

#solution-7
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {vowel_count}")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    print(f"GCD of {a} and {b} is: {a}")

def find_second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    if len(unique_numbers) < 2:
        print("List must have at least two unique numbers.")
        return
    unique_numbers.sort(reverse=True)
    print(f"The second largest number is: {unique_numbers[1]}")

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \n3. Check Palindrome \n4. Count Vowels \n5. Find GCD \n6. Find Second Largest \nEnter 1, 2, 3, 4, 5, or 6: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
elif choice == "3":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == "4":
    s = input("Enter a string: ")
    count_vowels(s)
elif choice == "5":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    find_gcd(a, b)
elif choice == "6":
    lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    find_second_largest(lst)
else:
    print("Invalid choice.")

#solution-8
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {vowel_count}")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    print(f"GCD of {a} and {b} is: {a}")

def find_second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    if len(unique_numbers) < 2:
        print("List must have at least two unique numbers.")
        return
    unique_numbers.sort(reverse=True)
    print(f"The second largest number is: {unique_numbers[1]}")

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \n3. Check Palindrome \n4. Count Vowels \n5. Find GCD \n6. Find Second Largest \nEnter 1, 2, 3, 4, 5, or 6: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
elif choice == "3":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == "4":
    s = input("Enter a string: ")
    count_vowels(s)
elif choice == "5":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    find_gcd(a, b)
elif choice == "6":
    lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    find_second_largest(lst)
else:
    print("Invalid choice.")

#solution-9
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching a ball"

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {vowel_count}")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    print(f"GCD of {a} and {b} is: {a}")

def find_second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    if len(unique_numbers) < 2:
        print("List must have at least two unique numbers.")
        return
    unique_numbers.sort(reverse=True)
    print(f"The second largest number is: {unique_numbers[1]}")

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \n3. Check Palindrome \n4. Count Vowels \n5. Find GCD \n6. Find Second Largest \nEnter 1, 2, 3, 4, 5, or 6: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
elif choice == "3":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == "4":
    s = input("Enter a string: ")
    count_vowels(s)
elif choice == "5":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    find_gcd(a, b)
elif choice == "6":
    lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    find_second_largest(lst)
else:
    print("Invalid choice.")

#solution-10
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching a ball"

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_description(self):
        return f"{self.title} by {self.author}, Pages: {self.pages}"

class BankAccount:
    def __init__(self, starting_balance):
        self.__balance = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def count_digits_in_string(s):
    digit_count = sum(1 for char in s if char.isdigit())
    print(f"Total digits are: {digit_count}")

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels: {vowel_count}")

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    print(f"GCD of {a} and {b} is: {a}")

def find_second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    if len(unique_numbers) < 2:
        print("List must have at least two unique numbers.")
        return
    unique_numbers.sort(reverse=True)
    print(f"The second largest number is: {unique_numbers[1]}")

# Take input from user
choice = input("Choose an operation: \n1. Multiplication Table \n2. Count Digits in String \n3. Check Palindrome \n4. Count Vowels \n5. Find GCD \n6. Find Second Largest \nEnter 1, 2, 3, 4, 5, or 6: ")

if choice == "1":
    n = int(input("Enter an integer: "))
    print_multiplication_table(n)
elif choice == "2":
    s = input("Enter a string: ")
    count_digits_in_string(s)
elif choice == "3":
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice == "4":
    s = input("Enter a string: ")
    count_vowels(s)
elif choice == "5":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    find_gcd(a, b)
elif choice == "6":
    lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    find_second_largest(lst)
else:
    print("Invalid choice.")