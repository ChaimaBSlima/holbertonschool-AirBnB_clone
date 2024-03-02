#!/usr/bin/python3
"""
Module for console
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    control the command
    """
    prompt = "(hbnb)"
    my_classes = ["BaseModel"]

    """ Task 6 functions"""
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

    """ Task 7 functions"""
    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        else:
            chaima = BaseModel()
            chaima.save()
            print(chaima.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            chaima = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in chaima:
                print(chaima[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            chaima = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in chaima:
                del chaima[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        chaima = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for i, j in chaima.items():
                print(str(j))
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        else:
            for i, j in chaima.items():
                if i.split('.')[0] == commands[0]:
                    print(str(j))

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute."
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            chaima = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in chaima:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = chaima[key]
                attribute_name = commands[2]
                attribute_value = commands[3]
                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass
                setattr(obj, attribute_name, attribute_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
