import random
import string
def genpass(length):
    if length < 6:
        print("Please enter a length of at least 6 characters.")
    else:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for i in range(length))
        print(f"Generated password: {password}")

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    genpass(length)

