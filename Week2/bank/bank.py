balance = 0


def get_balance():
    return balance


def deposit_money(amount):
    global balance
    if amount < 0:
        return False
    balance += amount
    return True


def withdraw_money(amount):
    global balance
    if amount < 0:
        return False
    if amount > balance:
        return False
    balance -= amount
    return True
