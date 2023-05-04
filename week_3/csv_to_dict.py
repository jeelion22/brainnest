"""    2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be a key-value pair in the dictionary.
"""


def convert_csv_to_dict():
    """Returns a dictionary as each row of the csv file as a key-value pair such that
    first element of the row as key, and rest of the element in the row as a value"""

    from os import getcwd
    import csv

    file_name = input("\nEnter a .csv file: ")

    try:
        file = open(file_name)

        csv_reader = csv.reader(file)

        print("\nconverting to dictionary...\n")

        dict_csv = {}

        for row in csv_reader:
            dict_csv[row[0]] = row[1:]

        return dict_csv

    except FileNotFoundError:
        print(f"\nFile '{file_name}' is not found in the directory '{getcwd()}'.\n")


if __name__ == "__main__":
    print(convert_csv_to_dict())
