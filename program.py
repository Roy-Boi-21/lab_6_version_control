# Name: David Visbal Gomez


def encode(passcode):
    new_passcode = ""
    for character in passcode:
        if ord(character) + 3 <= 57:
            new_passcode += chr(ord(character) + 3)
        else:
            new_passcode += chr(ord(character) - 7)
    return new_passcode


def decode(passcode):
    new_passcode = ""
    for character in passcode:
        if ord(character) - 3 >= 48:
            new_passcode += chr(ord(character) - 3)
        else:
            new_passcode += chr(ord(character) + 7)
    return new_passcode


def main():
    encoded_passcode = ""
    valid_passcode = True

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
            valid_passcode = True
            for character in password:
                if not character.isdigit():
                    valid_passcode = False
                    break
            if valid_passcode:
                encoded_passcode = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid passcode!  Only input integers please.")
        elif choice == "2":
            print(f"The encoded password is {encoded_passcode}, and the original password is {decode(encoded_passcode)}.")
        elif choice == "3":
            break
        else:
            print("Invalid input!")


main()
