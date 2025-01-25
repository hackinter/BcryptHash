import bcrypt
import getpass
import os
from time import sleep
from tqdm import tqdm

# Dummy user login system (for educational purposes)
users = {
    "admin": b"$2a$04$aF7ehXwwvWoBRlLGgrar9eZeF7d9a6hLLGrCd423geglRonEjyVlO",  # Hashed password for 'admin'
}

# Function to verify bcrypt hash match
def verify_bcrypt_hash(hashed_password, original_password):
    try:
        if bcrypt.checkpw(original_password.encode(), hashed_password):
            return True
    except ValueError:
        print("\033[1;31mInvalid bcrypt hash format.\033[0m")
    return False

# Function to generate a random bcrypt hash
def generate_bcrypt_hash():
    password = getpass.getpass("\033[1;32mEnter a password to hash: \033[0m")
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    print(f"\033[1;32mGenerated Hash: {hashed.decode()}\033[0m")

# Function to verify a bcrypt hash
def bcrypt_hash_verifier():
    hashed_password = input("\033[1;32mEnter the bcrypt hash: \033[0m")
    original_password = getpass.getpass("\033[1;32mEnter the password to verify: \033[0m")
    if verify_bcrypt_hash(hashed_password.encode(), original_password):
        print("\033[1;32mPassword matches the hash!\033[0m")
    else:
        print("\033[1;31mPassword does not match the hash.\033[0m")

# Function for brute-forcing bcrypt hash
def bcrypt_brute_force(hashed_password, wordlist_path):
    print("\033[1;34mStarting brute force...\033[0m")
    try:
        with open(wordlist_path, "r", encoding="latin-1") as wordlist:
            words = wordlist.readlines()
            for word in tqdm(words, desc="\033[1;36mAttempting passwords\033[0m", unit="password"):
                word = word.strip()
                if verify_bcrypt_hash(hashed_password.encode(), word):
                    print(f"\033[1;32mPassword found: {word}\033[0m")
                    return True
        print("\033[1;31mPassword not found in wordlist.\033[0m")
    except FileNotFoundError:
        print(f"\033[1;31mWordlist file not found: {wordlist_path}\033[0m")
    return False

# User Authentication (Persistent Login)
authenticated = False

def authenticate_user():
    global authenticated
    if authenticated:
        return True
    print("\033[1;34m⚡ Please enter your password ⚡\033[0m")
    password = getpass.getpass("\033[1;32mEnter password: \033[0m")
    username = "admin"  # Assuming the username is 'admin'
    if username in users and verify_bcrypt_hash(users[username], password):
        print("\033[1;32mLogin successful! 🎉\033[0m")
        authenticated = True
        return True
    else:
        print("\033[1;31mInvalid password. Please try again. ❌\033[0m")
        return False

# Main Menu
def main():
    while True:
        if not authenticate_user():
            continue
        print("\033[1;34mWelcome to the Bcrypt Tool\033[0m\n")
        sleep(1)
        print("1. Generate Random Bcrypt Hash")
        print("2. Bcrypt Hash Verifier")
        print("3. Bcrypt Hash Brute Force (Educational Purpose Only)")
        print("4. Help")
        print("5. Exit")

        choice = input("\033[1;36mChoose an option (1-5): \033[0m")

        if choice == '1':
            generate_bcrypt_hash()
        elif choice == '2':
            bcrypt_hash_verifier()
        elif choice == '3':
            print("\033[1;35mThis option is for educational purposes only. \033[0m")
            hashed_password = input("\033[1;32mEnter the bcrypt hash: \033[0m")
            wordlist_path = input("\033[1;32mEnter the path to the wordlist: \033[0m")
            bcrypt_brute_force(hashed_password, wordlist_path)
        elif choice == '4':
            print("\033[1;34mHelp Section:\033[0m\n")
            print("1: Generate a random bcrypt hash for a given password.")
            print("2: Verify if a password matches a given bcrypt hash.")
            print("3: Attempt to brute force a bcrypt hash using a wordlist.")
            print("5: Exit the tool.")
        elif choice == '5':
            print("\033[1;31mExiting the tool. Goodbye! 👋\033[0m")
            break
        else:
            print("\033[1;31mInvalid option, please try again.\033[0m")

if __name__ == "__main__":
    main()
