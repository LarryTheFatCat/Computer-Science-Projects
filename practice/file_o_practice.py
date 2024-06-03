"""
author: Tarkan Zarrouk
date: 04/23/2024
A skeleton file for a python project
"""


def main():
    # Input
    input_file_name = input("Enter the file name: ")
    input_author = input("Enter the author: ")
    input_date = input("Enter the date: ")
    input_description = input("Enter a description: ")

    # Processing
    file_name = input_file_name + ".py"
    with open(file_name, mode="w") as f_out:
        f_out.write(
            f'"""\nauthor: {input_author}\ndate: {input_date}\n{input_description}\n"""\n\n')
        f_out.write('def main():\n')
        f_out.write('    # Input\n')
        f_out.write('    # Processing\n')
        f_out.write('    # Output\n\n')
        f_out.write('if __name__ == "__main__":\n')
        f_out.write('    main()\n')
    # Output


if __name__ == "__main__":
    main()
