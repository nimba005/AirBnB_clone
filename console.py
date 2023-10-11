#!/usr/bin/python3

"""The ABNB console command interpreter"""

import cmd
from shlex import split
import re
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """defines the hbnb interpreter"""
    prompt = "(hbnb) "
    classes = {"BaseModel"}

    def do_create(self, arg):
        """creates a new instance of base model"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

    def do_quit(self, arg):
        """quiting the shell"""
        print("quitting the shell...")
        return (True)

    def do_EOF(self, arg):
        """end of file to exit"""
        print("quitting the shell...")
        return (True)

    def emptyline(self):
        """do nothing when an empty line"""
        pass

    def do_show(self,arg):
        """representation of an instance of basemodel"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(arg) != 2:
                print("** instance id missing **")
            else:
                for key, value in storage.all().items():
                    if arg[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on a class"""
        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if arg[0] == value.id:
                del storage.all()[key]
                storage.save()
                return
            print("** no instance found **") 
            
    def do_all(self, arg):
        """string representation of a class instance"""
        if not arg:
            print("** class name missing **")
            return

        arg = arg.split(' ')
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            objects = storage.all()
            instances = []
            for key, value in  objects.items():
                obj_name == value.__class__.__name__

                if obj_name == arg[0]:
                    instances += [value.__str__()]
            print(instances)






if __name__ == '__main__':
    HBNBCommand().cmdloop()
