import itertools
import string
import time

chars = string.ascii_letters + string.digits + "!@#$%^&*"

password = input("Enter the password: ")

def password_cracker(password):
    print("\nStarting Cracking...\n")

    start_time = time.time()
    attempts = 0

    # Only try combinations that match the length of the given password
    for combination in itertools.product(chars, repeat=len(password)):

        guess = ''.join(combination)
        attempts += 1

        print(f"Trying... {guess} | Attempt: {attempts}")

        if guess == password:
            elapsed = time.time() - start_time

            print("\n==============================")
            print("       PASSWORD CRACKED")
            print("==============================")
            print("Password :", guess)
            print("Attempts :", attempts)
            print("Time     :", round(elapsed, 4), "seconds")

            return

    print("\nPassword could not be cracked.")


if __name__ == "__main__":
    password_cracker(password)