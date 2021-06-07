# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os


class DslMain:

    file_name = ''
    file_path = ''

    def __init__(self, dir_path):
        self.file_path = dir_path
        self.file_name = DslMain.get_file(self)

    def get_file(self):
        if os.listdir(self.file_path) != '':
            self.file_name = self.file_path + '/' + os.listdir(self.file_path)[0]
            return self.file_name
        else:
            print('The file location is wrong.')
            return ''
        # file_name = './dsl_files/' + file_name

    def load_file(self, file):
        # Use a breakpoint in the code line below to debug your script.
        # file_path = 'dsl_files/' + file_name
        with open(file, 'r') as dsl_file:
            data = dsl_file.read()
            if data != '':
                print('The DSL file has been read.')
                print('Length of file is', len(str(data)))
                # print('File content is - ', '\n', data)
                return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Dsl_obj = DslMain('./dsl_files')
    file_path = Dsl_obj.get_file()
    Dsl_obj.load_file(file_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
