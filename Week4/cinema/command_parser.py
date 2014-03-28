class CommandParser():
    """docstring for CommandParser"""
    def __init__(self):
        self.functions = {}

    def on(self, command, callback):
        self.functions[command] = callback

    def take_command(self, unparsed_command):
        command_parts = unparsed_command.split(" ")
        arguments = command_parts[1:]

        if command_parts[0] in self.functions:
            self.functions[command_parts[0]](arguments)
