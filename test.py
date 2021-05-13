import pytest
from main import DslMain


def test_method():
    dsl_obj = DslMain('./dsl_files')
    filename = dsl_obj.file_name
    print('this is inside test.py - ', filename)
    file_content = dsl_obj.load_file(filename)
    assert file_content.find('workspace') != -1


if __name__ == '__main__':
    test_method()
