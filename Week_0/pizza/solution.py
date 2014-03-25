import os
from time import time
from datetime import datetime

### GLOBAL VARS ###
order = {}
saved = False
discard = False
current_orders_files = {}
#### END ###


### COMMANDS ###
def unknown_command():
    print("Unknown command!")
    print("Try one of the following:")
    print(" take <name> <price>")
    print(" status")
    print(" save")
    print(" list")
    print(" load <number>")
    print(" finish")


def take(name, price):
    global saved

    if name not in order:
        order[name] = price
    else:
        order[name] += price
    print("Taking order from %s for %s" % (name, price))
    saved = False


def status():
    for name in order:
        print("%s - %s" % (name, order[name]))


def save():
    global saved

    if len(order) == 0:
        print("Your order is empty.")
        return

    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "orders_" + stamp
    f = open(filename, "w")
    for name in order:
        row = name + "-" + str(order[name]) + '\n'
        f.write(row)
    f.close()

    print("Saved current order to %s" % (filename))
    saved = True


def c_list():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if len(files) == 1:
        print("No files.")
        return
    count = 1
    for f in files:
        if f != 'solution.py':
            current_orders_files[count] = f
            print("%s - %s" % (count, f))
            count += 1


def load(number):
    global order
    order = {}
    number = int(number)
    if number in current_orders_files:
        print("Loading %s" % (current_orders_files[number]))
        f = open(current_orders_files[number], 'r')
        contents = f.read().split("\n")
        for row in contents:
            if row != '':
                data = row.split("-")
                order[data[0]] = data[1]
        f.close()
    else:
        print("No such file. Use list command to see available files.")
#### END ###


def main():
    valid_commands = ['take', 'status', 'save', 'list', 'load', 'finish']
    exit = False
    global saved
    discard = False

    while not exit:
        command = input("Enter command>")
        command_split = command.split(" ")
        main_command = command_split[0]
        args = command_split[1:]

        if main_command not in valid_commands:
            unknown_command()
        elif main_command == 'take':
            if len(args) != 2:
                print("Invalid number of arguments (2) for take command.")
            else:
                take(args[0], float(args[1]))
            discard = False
        elif main_command == 'status':
            status()
            discard = False
        elif main_command == 'save':
            save()
            saved = True
            discard = False
        elif main_command == 'list':
            c_list()
            discard = False
        elif main_command == 'load':
            if len(args) != 1:
                print("Invalid number of arguments (1) for load command")
            elif len(current_orders_files) == 0:
                print("Use list command before loading")
            elif len(order) > 0 and not saved:
                if discard is False:
                    print("You have not saved the current order.")
                    print("If you wish to discard it, type load <number> again.")
                    discard = True
                else:
                    load(args[0])
                    discard = False
            else:
                load(args[0])
        elif main_command == 'finish':
            if len(order) > 0 and not saved:
                if discard is False:
                    print("You have not saved your order.")
                    print("If you wish to continue, type finish again")
                    print("If you want to save your order, type save")
                    discard = True
                else:
                    print("Finishing order. Goodbye!")
                    break
            else:
                print("Finishing order. Goodbye!")
                break


if __name__ == '__main__':
    main()
