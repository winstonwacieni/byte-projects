def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            ciphered_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += ciphered_char
        else:
            result += char
    return result

def write_to_file(ciphered_text):
    filename = input("Enter the filename to save the ciphered text: ")
    with open(filename, "w") as file:
        file.write(ciphered_text)
    print("Ciphered text saved to", filename)

def main():
    #add dafault and set it to 3
    # adds to the point >> You can jump in to python at Functions
    text = input(" Plaintext: ")
    shift = int(input("shift value:"))
    ciphered_text = caesar_cipher(text, shift)
    print("Ciphered text:", ciphered_text)
    write_to_file(ciphered_text)

if __name__ == "__main__":
    main()
