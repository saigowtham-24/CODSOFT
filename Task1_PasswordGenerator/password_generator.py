import random
import string

def generate_password(length):
    characters=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password

try:
    user_length=int(input("Enter desired password length: "))
    if user_length<4:
        print("Password length should be at least 4 characters.")
    else:
        print("Generated Password: ",generate_password(user_length))
except ValueError:
    print("Please enter a valid number.")