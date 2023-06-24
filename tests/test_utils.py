import src.operation
from src.utils import *

FILE_URL_GENERAL = "C:/forpy/bank/json_files/operations.json"
FILE_URL_TEST = "C:/forpy/bank/json_files/test.json"


def test_load_file():
    assert type(load_file(FILE_URL_GENERAL)) is list
    assert type(load_file(FILE_URL_TEST)) is list


def test_make_operations():
    first_list = load_file(FILE_URL_GENERAL)
    second_list = load_file(FILE_URL_TEST)

    for object in make_operations(first_list):
        assert type(object) is src.operation.Operation

    for object in make_operations(second_list):
        assert type(object) is src.operation.Operation

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
    assert get_all_operations(objects) == "26.08.2019 Перевод организации\n" \
                                         "Maestro 1596 83** **** 5199 -> Счет **9589\n" \
                                         "31957.58 руб.\n\n" \
                                         "03.07.2019 Перевод организации\n" \
                                         "MasterCard 7158 30** **** 6758 -> Счет **5560\n" \
                                         "8221.37 USD\n\n" \
                                         "04.04.2019 Перевод со счета на счет\n" \
                                         "Счет **8542 -> Счет **4188\n" \
                                         "79114.93 USD\n\n" \
                                         "23.03.2019 Перевод со счета на счет\n" \
                                         "Счет **4719 -> Счет **1160\n" \
                                         "43318.34 руб.\n\n" \
                                         "23.03.2018 Открытие вклада\n" \
                                         "Неизвестно -> Счет **2431\n" \
                                         "48223.05 руб.\n\n"


def test_get_executed_five():
    operations_list = load_file(FILE_URL_TEST)
    objects = make_operations(operations_list)
    assert get_executed_five(objects) == "26.08.2019 Перевод организации\n" \
                                         "Maestro 1596 83** **** 5199 -> Счет **9589\n" \
                                         "31957.58 руб.\n\n" \
                                         "03.07.2019 Перевод организации\n" \
                                         "MasterCard 7158 30** **** 6758 -> Счет **5560\n" \
                                         "8221.37 USD\n\n" \
                                         "04.04.2019 Перевод со счета на счет\n" \
                                         "Счет **8542 -> Счет **4188\n" \
                                         "79114.93 USD\n\n" \
                                         "23.03.2019 Перевод со счета на счет\n" \
                                         "Счет **4719 -> Счет **1160\n" \
                                         "43318.34 руб.\n\n" \
                                         "23.03.2018 Открытие вклада\n" \
                                         "Неизвестно -> Счет **2431\n" \
                                         "48223.05 руб.\n\n"
