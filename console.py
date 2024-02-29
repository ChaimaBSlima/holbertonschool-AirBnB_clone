#!/usr/bin/python
"""
Module for console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    control the command
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self, arg):
        """
        print the act of quit
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        just print the prompt again.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
