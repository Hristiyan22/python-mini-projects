
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encryption():
    while True:
        max_key = len(alphabet) - 1

        print(f"Please enter a key (0 to {max_key})")
        response = input("> ")

        if not response.isdigit():
            print("Please enter a digit!")
        elif not 0 <= int(response) < len(alphabet):
            print(f"The number must be between 0 and {max_key}!")
        else:
            key = int(response)
            break

    print("Enter message to encrypt: ")
    message = input("> ")
    message = message.lower()

    encrypted_message = ""
    for letter in message:
        if letter in alphabet:
            num = alphabet.find(letter)
            num += key

            if num >= len(alphabet):
                num -= len(alphabet)

                encrypted_message +=alphabet[num]
        else:
            encrypted_message += letter




def decryption():
    pass


def main():
    print("Welcome to the Ceaser encryption/decryption system!\n")

    while True:
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            encryption()
        elif choice == '2':
            decryption()
        elif choice == '3':
            print("Thank you for using the system! See you soon!")
            break
        else:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
