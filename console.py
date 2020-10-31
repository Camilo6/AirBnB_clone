#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""

import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


""" Classes """
CLASS = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """ Commands interpreter """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def empty_line(self, arg):
        """Empty line shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if len(arg) < 1:
            print("** class name missing **")
            return False

        arg_split = arg.split() #Split arguments
        if arg_split[0] in CLASS: #Include argument created in CLASS
            # Passing created argument to a new instance
            new_inst = CLASS[arg_split[0]]()
            new_inst.save() #Save the new instance in JSON file
            print(new_inst.id)
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        arg_split = arg.split()
        if len(arg_split) < 1:
            print("** class name missing **")
            return False

        if arg_split[0] not in CLASS:
            print("** class doesn't exist **")
            return False

        if len(arg_split) == 1:
            print("** instance id missing **")
            return False
            # NOT FINISHED YET
        storage = FileStorage()
        storage.reload()
        datas = storage.all()
        key = "{}.{}".format(arg_split[0], arg_split[1])
        if key not in datas.keys():
            print("** no instance found **")
            return False
        print(datas[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """

        arg_split = arg.split()
        if len(arg_split) == 0:
            print("** class name missing **")
            return False

        if len(arg_split) == 1:
            print("** instance id missing **")
            return False

        if arg_split[0] not in CLASS:
            print("** class doesn't exist **")

        storage = FileStorage()
        storage.reload()
        data = storage.all()
        key = "{}.{}".format(arg_split[0], arg_split[1])
        if key not in data.keys():
            print("** no instance found **")
            return False
        #Deletes data and save in JSON file
        del data[key]
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()