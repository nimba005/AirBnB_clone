#!/usr/bin/python3

"""The ABNB console command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """defines the hbnb interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quiting the shell"""
        print("quitting the shell...")
        return (True)

    def do_EOF(self, line):
        """end of file to exit"""
        print("quitting the shell...")
        return (True)

    def emptyline(self):
        """do nothing when an empty line"""
        pass




if __name__ == '__main__':
    HBNBCommand().cmdloop()
