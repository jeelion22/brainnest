"""
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call this technique a brute-force attack.
"""


def decryptCaesarCipher():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    usr_msge = input("Enter the message to decrypt.\n").upper()

    print("\ndecrypting your message...\n")

    for key in range(1, 27):
        decrypted_msge = ""
        for char in usr_msge:
            if char in alphabet:
                indx = alphabet.index(char) - key
                if indx <= 26:
                    decrypted_msge += alphabet[indx]

                else:
                    decrypted_msge += alphabet[indx + 26]

            else:
                decrypted_msge += char

        print(decrypted_msge)


decryptCaesarCipher()
