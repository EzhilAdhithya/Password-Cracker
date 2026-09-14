import time
import random
import string

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=-`~[]{};':,./<>?'~\"\|\""

password = input("Enter the password : ")

def password_cracker():
    print("\nStarting Cracking...\n")

    guess = ""

    while guess != password:

        guess = ""

        for i in range(len(password)):
            guess += random.choice(chars)
        
        print("Trying....!",guess)
        time.sleep(0.01)

        if guess == password:
            print("\nPassword Cracked : ",guess)

if __name__ == "__main__":
    password_cracker()