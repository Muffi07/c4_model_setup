import math

from main import DslMain

import os

dsl_obj = DslMain('./dsl_files')

# xml_file_name = ''


def test_dsl_file_check():
    # dsl_obj = DslMain('./dsl_files')
    filename = dsl_obj.file_name
    print('Before 1st assert-----1111111111111')
    assert filename != ''


def test_dsl_file_content():
    # dsl_obj = DslMain('./dsl_files')
    filename = dsl_obj.file_name
    file_content = dsl_obj.load_file(filename)
    print('Before 2nd assert-----2222222222222')
    assert len(file_content) > 1


def test_dsl_file_url():
    # dsl_obj = DslMain('./dsl_files')
    filename = dsl_obj.file_name
    file_content = dsl_obj.load_file(filename)

    print('Before 2nd assert-----2222222222222')
    if file_content.find('url') != -1:
        file_content_list = file_content.split('\n')
        line_num = len(file_content_list) - 1
        print('Inside 1st if     ++++++++++++')
        while line_num > 0:
            # print(line_num)
            if file_content_list[line_num].find('url') != -1:
                # print('Inside if of line condition ', line_num)
                break
            line_num = line_num - 1
        # print('Inside innermost if.')
        print(file_content_list[line_num][-4:])
        if file_content_list[line_num][-4:] != '.xml':
            assert False, "Test Report file name is not present in the DSL file"
    else:
        assert False, "URL is not present in the DSL file"
    assert True, "URL and Report file is present in the DSL file"


def test_dsl_file_report_check():
    # dsl_obj = DslMain('./dsl_files')
    filename = dsl_obj.file_name
    file_content = dsl_obj.load_file(filename)
    file_content_list = file_content.split('\n')

    line_num = len(file_content_list) - 1
    print('Inside 1st if     ++++++++++++')
    while line_num > 0:
        # print(line_num)
        if file_content_list[line_num].find('url') != -1:
            # print('Inside if of line condition ', line_num)
            break
        line_num = line_num - 1

    xml_file_name_start = file_content_list[line_num].rfind('/') + 1
    xml_file_name = file_content_list[line_num][xml_file_name_start:]
    print('xml_file_name is - ', xml_file_name)
    current_dir = os.path.abspath(os.getcwd())
    print('This is current working directory path - ', current_dir)
    ext_report_xml_dir = current_dir + '\\external_report_xmls'
    print(os.listdir(ext_report_xml_dir))
    if xml_file_name in os.listdir(ext_report_xml_dir):
        assert True, "Test Report XML file found."
    else:
        assert False, "Test Report XML file NOT found."


# pytest pytest_01.py -v --junitxml=dng.xml

if __name__ == '__main__':
    # dsl_obj = DslMain('./dsl_files')
    print('It is inside main of pytest--------')
    test_dsl_file_check()
    test_dsl_file_content()
    test_dsl_file_url()
    test_dsl_file_report_check()
