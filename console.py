#!/usr/bin/python3

"""The ABNB console command interpreter"""

import cmd
from shlex import split
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """defines the hbnb interpreter"""
    prompt = "(hbnb) "
    classes = {"BaseModel","User", "State",
            "City", "Amenity", "Place", "Review"}

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

    def default(self, arg):
        """Handle commands that are not defined"""
        methods = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        if ".all" in arg or ".count" in arg:
            args = arg.split(".")
            class_name = args[0]
            method_name = args[1][:-2]
            if class_name in self.classes and method_name in methods:
                methods[method_name](class_name)
            else:
                print("** Unknown syntax: {} **".format(arg))
        elif ".show" in arg:
            command = arg.split(".")
            class_name = command[0]
            id = command[1][6:-2]
            self.do_show(class_name + " " + id)
        elif ".destroy" in arg:
            command = arg.split(".")
            class_name = command[0]
            id = command[1][9:-2]
            self.do_destroy(class_name + " " + id)
        elif ".update" in arg:
            command = arg.split(".")
            class_name = command[0]
            values = command[1].split(",")
            id = values[0][8:-2]
            attr_name = values[1][2:-1]
            new_value = values[2][2:-2]
            self.do_update(
                class_name + " " + id + " " + attr_name + " " + new_value)
        else:
            print("** Unknown syntax: {} **".format(arg))

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            count = len(
                [obj for key, obj in all_objs.items()
                 if key.startswith(arg[0])]
                        )
            print(count)


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
        args = split(arg)
        all_objs = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objs.items()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if arg[0].endswith('.all'):
                class_name = arg[0].split(".")[0]
                class_objs = [
                    value for key, value in all_objs.items()
                    if key.startswith(class_name)]
                strs = [str(obj) for obj in class_objs]
                print(strs)
            else:
                class_objs = [
                    value for key, value in all_objs.items()
                    if key.startswith(arg[0])]
                strs = [str(obj) for obj in class_objs]
                print(strs)


    def do_destroy(self, arg):
        """destroy an instance based on his ID"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            every_obj = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in every_obj:
                del every_obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """updates instances based on class names"""
        args = arg.split()
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
