# Vignere cipher

# This section encrypts the text by using the key
def encrypt():
    plain_text = input('Enter the text to encrypt: ')
    plain_text = plain_text.upper()
    length = len(plain_text)

    key = str(input('Enter the key: '))
    full_key = key.upper()*(1+(length//(len(key))))
    encrypt_char = []
    for index_no in range(0,length):
        plain_no = ord(plain_text[index_no])
        shift = (ord(full_key[index_no]) - 65)
        if 64 < plain_no < 91:
            encrypt_no = plain_no + shift
            if encrypt_no > 90:
                encrypt_no = (64 + (encrypt_no - 90))
        else:
            encrypt_no = plain_no
        encrypt_char.append(chr(encrypt_no))

    print('Plain text:',plain_text)
    encrypt_text = print('Encrypted text:',''.join(encrypt_char))

# This section decrypts the text by using the key
def decrypt():
    encrypt_text = input('Enter the text to decrypt: ')
    encrypt_text = encrypt_text.upper()
    length = len(encrypt_text)

    key = str(input('Enter the key: '))
    full_key = key.upper()*(1+(length//(len(key))))
    decrypt_char = []
    for index_no in range(0,length):
        encrypt_no = ord(encrypt_text[index_no])
        shift = (ord(full_key[index_no]) - 65)
        if 64 < encrypt_no < 91:
            plain_no = encrypt_no - shift
            if plain_no < 65:
                plain_no = (91 - (65 - plain_no))
        else:
            plain_no = encrypt_no
        decrypt_char.append(chr(plain_no))

    print('Encrypted text:',encrypt_text)
    decrypt_text = print('Decrypted text:',''.join(decrypt_char))


selection = input('What do you want to do? Encrypt(E) or Decrypt(D): ')
if selection == 'e':
    encrypt()
elif selection == 'd':
    decrypt()