# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os


def load_file(file):
    # Use a breakpoint in the code line below to debug your script.
    # file_path = 'dsl_files/' + file_name
    with open(file, 'r') as dsl_file:
        data = dsl_file.read()
        if dsl_file != '':
            print('The DSL file has been read.')
            print('Length of file is', len(str(dsl_file)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if os.listdir('./dsl_files') != '':
        file_name = os.listdir('./dsl_files')[0]
    file_name = './dsl_files/' + file_name
    load_file(file_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
