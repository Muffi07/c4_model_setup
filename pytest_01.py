import math

from main import DslMain


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    # num = 7
    assert 7 * 7 == 49


def test_equality():
    assert 10 == 10


def dsl_file_check(m_dsl_obj):
    # dsl_obj = DslMain('./dsl_files')
    filename = m_dsl_obj.file_name
    assert filename != ''


def dsl_file_content(m_dsl_obj):
    filename = m_dsl_obj.file_name
    file_content = m_dsl_obj.load_file(filename)
    assert file_content.find('workspace') != -1


# pytest pytest_01.py -v --junitxml=result.xml
if __name__ == '__main__':
    dsl_obj = DslMain('./dsl_files')
    dsl_file_check(dsl_obj)
    dsl_file_content(dsl_obj)



    # test_method()
    # test_sqrt()
    # test_square()
    # test_equality()
