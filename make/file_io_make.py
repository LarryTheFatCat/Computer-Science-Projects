"""
author: Tarkan Zarrouk
date: 04/26/2024
madlibs game using python 
"""


def main():
    # input
    # read in file
    with open("game.txt", mode="r") as f_in:
        content = f_in.read()

    # processing
    # impl placeholders to be replaced
    placeholders = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

    # loop over placeholders array for input && replace
    for placeholder in placeholders:
        user_input = input(f"Enter an {placeholder}: ")
        content = content.replace(placeholder, user_input) # replace any preexisting contents
        
    # debug
    print(content)
        
    # output
    # write to new file
    with open("game.txt", mode="w") as f_out:
        f_out.write(content) # write out file


if __name__ == "__main__":
    main()
