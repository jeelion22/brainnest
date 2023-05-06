"""    3. Write a Python program that reads a binary file and converts it into a hexadecimal string. The program should output the hexadecimal string to a text file.
"""

from os import getcwd
import binascii


def convert_bin_to_hexa():
    """Converts .bin file as .txt file contains hexadecimal string. It generally converts all type data into hexadecimal string"""
    file_name = input("\nEnter a .bin file: ")

    try:
        bin_file = open(file_name, "rb")

        bin_data = bin_file.read()

        print("\nconverting to hexadecimal...\n")

        hexa_data = binascii.hexlify(bin_data)

        with open("bin_to_hexa.txt", "w") as txt_file:
            txt_file.write(hexa_data.decode("utf-8"))

        print("Conversion finished!\n")

        print(f"The file 'bin_to_hexa.txt' is found in the directory '{getcwd()}'.\n")

        txt_file.close()

    except FileNotFoundError:
        print(f"\nFile '{file_name}' is not found in the directory '{getcwd()}'.\n")

    except binascii.Incomplete:
        print(
            "Warning: The input data is not a multiple of the required block size for the conversion function."
        )


if __name__ == "__main__":
    convert_bin_to_hexa()
