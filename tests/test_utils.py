import src.operation
from src.utils import *


FILE_URL = "../json_files/operations.json"
FILE_URL_TEST = "../json_files/test.json"


def test_load_file():
    assert isinstance(load_file(FILE_URL), list)
    assert isinstance(load_file(FILE_URL_TEST), list)


def test_make_operations():
    first_list = load_file(FILE_URL)
    second_list = load_file(FILE_URL_TEST)

    for object in make_operations(first_list):
        assert isinstance(object, src.operation.Operation)

    for object in make_operations(second_list):
        assert isinstance(object, src.operation.Operation)

    assert make_operations(second_list)[0].get_id() == 441945886
    assert make_operations(second_list)[0].get_date() == "26.08.2019"
    assert make_operations(second_list)[0].get_state() == "EXECUTED"
    assert make_operations(second_list)[0].get_information() == "26.08.2019 Перевод организации\n" \
                                                                "Maestro 1596 83** **** 5199 -> Счет **9589\n" \
                                                                "31957.58 руб.\n\n"
    assert str(make_operations(second_list)[0]) == "операция 441945886"



def test_get_all_operations():
    operations_list = load_file(FILE_URL_TEST)
    objects = make_operations(operations_list)
    assert isinstance(objects, list)
    assert isinstance(objects[0]), Operation



def test_get_executed_five():
    operations_list = load_file(FILE_URL_TEST)
    objects = make_operations(operations_list)
    assert isinstance(objects, list)
    assert isinstance(objects[0]), Operation


