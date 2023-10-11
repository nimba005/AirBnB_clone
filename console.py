#!/usr/bin/python3

"""The ABNB console command interpreter"""

import cmd
from shlex import split
import re
from models import storage
from models.base_model import BaseModel
from models.user import User


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
            new_instance = eval(arg)()
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
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        objects = storage.all()
        value = objects.get(key, None)

        if value is None:
            print("** no instance found **")
        else:
            print(value)

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
                obj_name = value.__class__.__name__

                if obj_name == arg[0]:
                    instances += [value.__str__()]
            print(instances)

    def do_update(self, arg):
        """updates instances based on class names"""
        cmd_args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in HBNBCommand.classes:
            if len(arg) > 1:
                key = arg[0] + '.' + arg[1]
                if key in storage.all():
                    if len(arg) > 2:
                        if len(arg) > 3:
                            setattr(storage.all()[key], arg[2], arg[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
