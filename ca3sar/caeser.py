def caeser_cipher(text, shift):
    result= ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper()