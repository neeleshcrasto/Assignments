# Caeser cipher

# This section encrypts the text by shifting it right
plain_text = input('Enter the text to encrypt:')
plain_text = plain_text.upper()
shift = int(input('Enter the shift number:'))
encrypt_char = []
for char in plain_text:
    plain_no = ord(char)
    if 64 < plain_no < 91:
        encrypt_no = plain_no - shift
        if encrypt_no < 65:
            encrypt_no = (91 - (65 - encrypt_no))
    else:
        encrypt_no = plain_no
    encrypt_char.append(chr(encrypt_no))

print('Plain text:',plain_text)
encrypt_text = print(''.join(encrypt_char))

