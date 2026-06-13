alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(original_text, shift_amount):
    encoded_word = []

    for char in original_text:

        if char.lower() not in alphabet:
            encoded_word.append(char)
            continue

        is_upper = char.isupper()

        idx = alphabet.index(char.lower())
        new_idx = (idx + shift_amount) % len(alphabet)
        new_char = alphabet[new_idx]

        if is_upper:
            encoded_word.append(new_char.upper())
        else:
            encoded_word.append(new_char)

    print("".join(encoded_word))

def decrypt(encrypted_text, shift_amount):
    decoded_word = []

    for char in encrypted_text:

        if char.lower() not in alphabet:
            decoded_word.append(char)
            continue

        is_upper = char.isupper()

        idx = alphabet.index(char.lower())
        new_idx = (idx - shift_amount) % len(alphabet)
        new_char = alphabet[new_idx]

        if is_upper:
            decoded_word.append(new_char.upper())
        else:
            decoded_word.append(new_char)

    print("".join(decoded_word))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
