import sys
import platform
import time
from termcolor import colored

DEFAULT_SHIFT = 3
TIMEOUT = 3.5

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

def print_banner():
    banner = '''
  ___   _   _____   ____    ___    ___     ___    _   _ 
 |_ _| | | |_   _| |  _ \  |_ _|  / _ \   / _ \  | | | |
  | |  | |   | |   | | | |  | |  | | | | | | | | | | | |
  | |  | |   | |   | |_| |  | |  | |_| | | |_| | | |_| |
 |___| |_|   |_|   |____/  |___|  \___/   \___/   \___/  
    '''
    if platform.system() == "Windows":
        print(banner)
    else:
        print(colored(banner, "blue"))

def get_shift():
    try:
        shift = input("Enter the shift value (default: 3): ")
        if shift == '':
            shift = DEFAULT_SHIFT
        else:
            shift = int(shift)
        return shift
    except ValueError:
        print(colored("Invalid shift value. Using default shift of 3.", "yellow"))
        return DEFAULT_SHIFT

def main():
    print_banner()
    text = input("Enter the text to encrypt: ")

    try:
        shift = get_shift()
        time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        print(colored("\nTimeout exceeded. Using default shift of 3.", "yellow"))
        shift = DEFAULT_SHIFT

    ciphered_text = caesar_cipher(text, shift)
    print("Ciphered text:", colored(ciphered_text, "green"))
    write_to_file(ciphered_text)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\nProgram interrupted. Exiting...", "red"))
        sys.exit(0)
