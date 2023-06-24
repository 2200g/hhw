import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("pass length [def: 16]: "))
password = generate_password(password_length)
print("password: ", password)
