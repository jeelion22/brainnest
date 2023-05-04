""" 4. Write a Python program that reads a text file containing numbers and calculates the sum of all the numbers in the file. """

from os import getcwd
import re


def calculate_sum_of_numbers():
    """Prints the sum of the numbers in the file if the file presents in the current directory"""

    # gets file name from the user
    file_name = input("\nEnter a .txt file containing numbers for calculate sum: ")

    try:
        # pattern for numbers
        pattern = re.compile(r"-?[\d\.\d]+")

        with open(file_name) as txt_file:
            # assigns numbers list in numbers_list
            numbers_list = pattern.findall(txt_file.read())

            # sums the numbers in list after conversion to floats
            total = sum(map(float, numbers_list))

            print(f"The sum of all numbers in the file is {total}.")

    except FileNotFoundError:
        # prints message when file is not found
        print(f"\nFile '{file_name}' is not found in the directory '{getcwd()}'.\n")


if __name__ == "__main__":
    calculate_sum_of_numbers()
