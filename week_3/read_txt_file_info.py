"""1. Write a Python program that reads a text file and prints the number of lines, words, and characters in the file."""


def get_file_content_info():
    """prints the content info of the file that is found in the current
    directory
    """

    from os import getcwd

    file_name = input("\nEnter a .txt file: ")

    try:
        file = open(file_name, "r")

        print("\nreading...")

        lines = 0
        words = 0
        characters = 0

        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

        print(f"\nFile's Content Info\n")
        print("Number of lines: ", lines)
        print("Number of words: ", words)
        print("Number of characters: ", characters)
        print()

    except FileNotFoundError:
        print(f"File '{file_name}' is not found in the directory '{getcwd()}'.")


if __name__ == "__main__":
    get_file_content_info()
