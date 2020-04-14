# Caeser cipher

# This section encrypts the text by shifting it right
def encrypt():
    plain_text = input('Enter the text to encrypt: ')
    plain_text = plain_text.upper()
    shift = int(input('Enter the shift number: '))
    encrypt_char = []
    for char in plain_text:
        plain_no = ord(char)
        if 64 < plain_no < 91:
            encrypt_no = plain_no - shift
            if encrypt_no < 65:
                encrypt_no = (91 - (65 - encrypt_no))
        elif 47 < plain_no < 58:
            encrypt_no = plain_no - shift
            if encrypt_no < 48:
                encrypt_no = (58 - (48 - encrypt_no))
        else:
            encrypt_no = plain_no
        encrypt_char.append(chr(encrypt_no))

    print('Plain text:',plain_text)
    encrypt_text = print(''.join(encrypt_char))

# This section decrypts the encrypted text
def decrypt():
    encrypt_text = input('Enter the text to decrypt: ')
    encrypt_text = encrypt_text.upper()
    shift = int(input('Enter the shift number: '))
    decrypt_char = []
    for char in encrypt_text:
        encrypt_no = ord(char)
        if 64 < encrypt_no < 91:
            plain_no = encrypt_no + shift
            if plain_no > 90:
                plain_no = (64 + (plain_no - 90))
        elif 47 < encrypt_no < 58:
            plain_no = encrypt_no + shift
            if plain_no > 57:
                plain_no = (47 + (plain_no - 57))
        else:
            plain_no = encrypt_no
        decrypt_char.append(chr(plain_no))

    print('Encrypted text:',encrypt_text)
    decrypt_text = print(''.join(decrypt_char))


selection = input('What do you want to do? Encrypt(E) or Decrypt(D): ')
if selection == 'e':
    encrypt()
elif selection == 'd':
    decrypt()
