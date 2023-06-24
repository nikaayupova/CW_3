import json
import datetime

from src.operation import Operation

def load_file(file_url):
    with open(file_url, "r", encoding="UTF-8") as j_file:
        operations = json.load(j_file)
        return operations


def make_operations(operations: list):
    operations_list = []

    def check_wallet(where: str):
        wallet = "Неизвестно"
        try:
            card = inf[f'{where}']
            if card[:4] == "Счет":
                wallet = f"{card[:4]} **{card[-4:]}"
            else:
                wallet = f"{card[:-12]} {card[-12:-10]}** **** {card[-4:]}"
            return wallet
        except:
            return wallet

    for inf in operations:
        try:
            operation_id = inf["id"]
            state = inf["state"]
            date_full = datetime.datetime.strptime(inf["date"], "%Y-%m-%dT%H:%M:%S.%f")
            date = datetime.datetime.strftime(date_full, "%d.%m.%Y")
            description = inf["description"]
            sender = check_wallet("from")
            receiver = check_wallet("to")
            amount = inf["operationAmount"]["amount"]
            currency = inf["operationAmount"]["currency"]["name"]
            operation = Operation(operation_id, state, date, description, sender, receiver, amount, currency)
            operations_list.append(operation)
        except:
            continue
    return operations_list


def get_all_operations(operations: list):
    information = ''
    operations.sort(key=lambda x: datetime.datetime.strptime(x.get_date(), "%d.%m.%Y"), reverse=True)
    for operation in operations:
        information += operation.get_information()
    return information


def get_executed_five(operations: list):
    operations_counter = 0
    information = ''
    operations.sort(key=lambda x: datetime.datetime.strptime(x.get_date(), "%d.%m.%Y"), reverse=True)
    for operation in operations:
        if operation.state == "EXECUTED":
            operations_counter += 1
            information += operation.get_information()
        if operations_counter == 5:
            break
    return information





