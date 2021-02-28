#!/usr/bin/python3
"""Define Command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter
    Attributes:
        prompt (str): Command prompt.
    """
    prompt = "(hbnb) "
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_EOF(self, line):
        """To exit with Ctrl-D"""
        print("")
        return True

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_create(self, line):
        """Create instance of class"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Print the string representation of an instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = parse(line)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """delete an instance of a given id"""
        line1 = parse(line)
        objdict = storage.all()
        if len(line1) == 0:
            print("** class name missing **")
        elif line1[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(line1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line1[0], line1[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(line1[0], line1[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update attribute value"""
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg1 = args[3]
            arg1 = arg1.strip('"')
            arg1 = arg1.strip("'")
            setattr(storage.all()[key], args[2], cast(arg1))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
