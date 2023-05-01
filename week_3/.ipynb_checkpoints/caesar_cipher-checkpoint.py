"""
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

try:
    usr_inp = input("Do you want to (e)ncrypt or (d)ecrypt?\n")

    # encryption

    if usr_inp == "e":
        usr_key = int(input("Please enter the key (0 to 25) to use.\n"))

        if usr_key in range(0, 26):
            usr_msge = input("Enter the message to encrypt.\n").upper()

            encrypted_msge = ""

            for i in usr_msge:
                if i.isalpha():
                    indx = alphabet.index(i) + usr_key

                    if indx <= 25:
                        encrypted_msge += alphabet[indx]

                    else:
                        encrypted_msge += alphabet[indx - 26]
                else:
                    encrypted_msge += i

            print(encrypted_msge)
        else:
            print("Key is not in ranged.")

    # decryption

    elif usr_inp == "d":
        usr_key = int(input("Please enter the key (0 to 26) to use.\n"))

        if usr_key in range(0, 27):
            usr_msge = input("Enter the message to decrypt.\n").upper()

            decrypted_msge = ""

            for i in usr_msge:
                if i.isalpha():
                    indx = alphabet.index(i) - usr_key
                    if indx <= 25:
                        decrypted_msge += alphabet[indx]

                    else:
                        decrypted_msge += alphabet[indx + 26]

                else:
                    decrypted_msge += i

            print(decrypted_msge)

        else:
            print("Key is not in range.")

    else:
        print("Invalid Choice. Please enter either 'e' or 'd'.")

except ValueError:
    print("Invalid key. ")
