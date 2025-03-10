alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_mode():
    print("Welcome to the Caesar Cipher System!")
    while True:
        print("Menu:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            return "encrypt"
        elif choice == "2":
            return "decrypt"
        elif choice == "3":
            print("Thank you for using the system! See you soon!")
            return "exit"
        else:
            print("❌ Invalid choice. Try again!\n")


def get_key():
    """Prompt user to enter a valid shift key."""
    max_key = len(alphabet_lower) - 1
    while True:
        response = input(f"Enter a key (0 to {max_key}): ").strip()
        if response.isdigit():
            key = int(response)
            if 0 <= key <= max_key:
                return key
        print(f"❌ Invalid key. Please enter a number between 0 and {max_key}.\n")


def caesar_cipher(message, key, mode):
    result = ""
    for letter in message:
        if letter in alphabet_lower:
            alphabet = alphabet_lower
        elif letter in alphabet_upper:
            alphabet = alphabet_upper
        else:
            result += letter
            continue

        num = alphabet.find(letter)
        if mode == "encrypt":
            num = num + key
            if num >= len(alphabet):
                num -= len(alphabet)
        else:
            num = num - key
            if num < 0:
                num += len(alphabet)

        result += alphabet[num]
    return result


def main():
    while True:
        mode = get_mode()
        if mode == "exit":
            break
        key = get_key()
        message = input("Enter your message: ").strip()
        result = caesar_cipher(message, key, mode)
        print(f"\nResult: {result}\n")


if __name__ == "__main__":
    main()
