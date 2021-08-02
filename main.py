# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from DslFileCheck import DslFileCheck


class DslMain:
    file_name = ''
    file_path = ''

    def __init__(self, dir_path):
        self.file_path = dir_path

    def get_file(self):
        # print("filename check - ", os.listdir(self.file_path))
        if len(os.listdir(self.file_path)) > 0:
            self.file_name = self.file_path + '/' + os.listdir(self.file_path)[0]
            print('DSL file name is - ', self.file_name)
            return self.file_name
        else:
            # print('The file location is wrong.')
            assert False, 'The file location is wrong.'
        # file_name = './dsl_files/' + file_name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Dsl_obj = DslMain('./dsl_files')
    file_path = Dsl_obj.get_file()

    dslChk = DslFileCheck()

    file_data = dslChk.load_file(file_path)
    prod_dict = dslChk.dsl_file_product_chk()
    name_cont_dict, cont_dict, name_cont_map_dict, failed_cont_list = dslChk.dsl_file_container_chk()
    print(cont_dict, failed_cont_list)
    cont_relation_dict = dslChk.dsl_file_cont_relation()
    dslChk.dsl_file_depl_env()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
