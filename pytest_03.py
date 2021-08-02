import math

from main import DslMain

import os


class TestDslFile:
    file_name = ''
    xml_file_name = ''
    dsl_obj = None

    # def __init__(self, dsl_object):
    #     self.xml_file_name = ''
    #     self.dsl_obj = dsl_object

    def test_dsl_file_check(self, dsl_object):
        # dsl_obj = DslMain('./dsl_files')
        TestDslFile.dsl_obj = dsl_object
        TestDslFile.file_name = TestDslFile.dsl_obj.file_name
        print('Before 1st assert-----1111111111111')
        assert TestDslFile.file_name != ''

    def test_dsl_file_content(self):
        # dsl_obj = DslMain('./dsl_files')
        # filename = TestDslFile.dsl_obj.file_name
        file_content = TestDslFile.dsl_obj.load_file(TestDslFile.file_name)
        print('Before 2nd assert-----2222222222222')
        assert len(file_content) > 1

    def test_dsl_file_url(self):
        # dsl_obj = DslMain('./dsl_files')
        # filename = self.dsl_obj.file_name
        file_content = TestDslFile.dsl_obj.load_file(TestDslFile.file_name)

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
                assert False, "XML file path is not present in the DSL file"
            else:
                xml_file_name_start = file_content_list[line_num].rfind('/') + 1
                TestDslFile.xml_file_name = file_content_list[line_num][xml_file_name_start:]
                print('The xml_file_name inside test_dsl_file_url - ', TestDslFile.xml_file_name)
                assert True
        else:
            assert False, "URL is not present in the DSL file"

    def test_dsl_file_report_xml_check(self):
        print('This is inside last method ---- ', TestDslFile.xml_file_name)
        print('xml_file_name is - ', TestDslFile.xml_file_name)
        current_dir = os.path.abspath(os.getcwd())
        print('This is current working directory path - ', current_dir)
        ext_report_xml_dir = current_dir + '\\external_report_xmls'
        print(os.listdir(ext_report_xml_dir))
        if TestDslFile.xml_file_name in os.listdir(ext_report_xml_dir):
            assert True, "Test Report XML file found."
        else:
            assert False, "Test Report XML file NOT found."


# pytest pytest_01.py -v --junitxml=dng.xml

if __name__ == '__main__':
    # dsl_obj = DslMain('./dsl_files')
    dsl_dir = './dsl_files'

    dsl_obj = DslMain(dsl_dir)
    test_dsl_file_obj = TestDslFile
    print('It is inside main of pytest--------')
    test_dsl_file_obj.test_dsl_file_check(dsl_obj)
    test_dsl_file_obj.test_dsl_file_content()
    test_dsl_file_obj.test_dsl_file_url()
    test_dsl_file_obj.test_dsl_file_report_xml_check()
