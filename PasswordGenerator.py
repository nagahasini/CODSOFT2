import random
import string


def create_password(size):
    # Define character set: letters, numbers, and symbols
    char_set=string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the desired size
    return ''.join(random.choices(char_set, k=size))


def main():
    # Ask the user to input the desired password length
    try:
        length=int(input("Please enter the length of the password: "))
        if length <= 0:
            print("Password length must be greater than zero.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Generate and show the password
    password=create_password(length)
    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()
