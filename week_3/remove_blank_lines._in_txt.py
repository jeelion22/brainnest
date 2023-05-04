"""    5. Write a Python program that reads a text file and removes all the blank lines. The modified text should be written back to the file.
"""

from os import getcwd


def remove_blank_lines():
    # gets file name from the user
    file_name = input("\nEnter a .txt file to remove blank lines: ")

    try:
        # reads file
        with open(file_name, "r") as txt_file:
            lines = txt_file.readlines()

        print("removing empty lines...")

        # removes empty line
        new_lines = [line for line in lines if line.strip()]

        # rewriting file with new content
        with open(file_name, "w") as new_file:
            new_file.writelines(new_lines)

            new_file.close()

        print("File rewriting Completed ")

    except FileNotFoundError:
        # prints the message when file is not found
        print(f"\nFile '{file_name}' is not found in the directory '{getcwd()}'.\n")


if __name__ == "__main__":
    remove_blank_lines()
