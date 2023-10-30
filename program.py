# Name: David Visbal Gomez


def encode(passcode):
    new_passcode = ""
    for character in passcode:
        new_passcode += chr(ord(character) + 10)
    return new_passcode


def decode(passcode):
    new_passcode = ""
    for character in passcode:
        new_passcode += chr(ord(character) - 10)
    return new_passcode


def main():
    encoded_passcode = ""

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_passcode = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            print(f"The encoded password is {encoded_passcode}, and the original password is {decode(encoded_passcode)}.")
        elif choice == "3":
            break
        else:
            print("Invalid input!")


main()
