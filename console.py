#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (ctrl+D) is encountered"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def Default(self, line):
        """Default behavior for an unknown command"""
        if line == '':
            return
        print(f"*** Unknown command: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
