def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    balance = 0
    for i in brackets_row:
        if i == '(':
            balance += 1
        elif i == ')':
            balance += -1
            if balance < 0:
                return False
    return balance == 0
