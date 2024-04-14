# Daniel Permane

def encode(input):
    output = ""
    for i in input:
        encoded_char = (int(i) + 3) % 10
        output += str(encoded_char)
    return output

def decode(input):
    password = ""
    for char in input:
        decoded_char = int(char) - 3
        if decoded_char < 0:
            decoded_char += 10
        password += str(decoded_char)
    return password

def main():
    while True:
        encoded_password = ""

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option:"))

        if option == 1:
            encoded_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {decode(encoded_password)}, and the original password is {encoded_password}.")
        elif option == 3:
            break


if __name__ == "__main__":
    main()
