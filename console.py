#!/usr/bin/python3
"""Program that contains the entry point of the command interpreter"""

from models.base_model import BaseModel
import cmd
import shlex
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


""" Classes """
CLASS = {"BaseModel": BaseModel, "User": User,
         "City": City, "Place": Place, "Review": Review,
         "State": State, "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    """ Commands interpreter """
    prompt = "(hbnb) "

    def do_update(self, arg):
            """
            Update specific attribute of a class instance of
            a given <id> Usage:
            update <class name> <id> <attribute name> "<attribute value>"
            """
            arg_split = arg.split()

            if not len(arg_split):
                print("** class name missing **")
                return False

            if arg_split[0] not in CLASS:
                print("** class doesn't exist **")
                return False

            if len(arg_split) == 1:
                print("** instance id missing **")
                return False

            if len(arg_split) == 2:
                print("** attribute name missing **")
                return False

            if len(arg_split) == 3:
                print("** value missing **")
                return False

            else:
                storage = FileStorage()
                data = storage.all()
                key = "{}.{}".format(arg_split[0], arg_split[1])
                if key in data.keys():
                    setattr(data[key], arg_split[2], arg_split[3])
                    storage.save()
                else:
                    print("** no instance found **")
                    return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def empty_line(self, arg):
        """Empty line shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if len(arg) < 1:
            print("** class name missing **")
            return False

        arg_split = arg.split()  # Split arguments
        if arg_split[0] in CLASS:  # Include argument created in CLASS
            # Passing created argument to a new instance
            new_inst = CLASS[arg_split[0]]()
            new_inst.save()  # Save the new instance in JSON file
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
        # Deletes data and save in JSON file
        del data[key]
        storage.save()

    def do_all(self, arg):
        """
        Shows all objects, or all objects of a class
        """
        arg_split = arg.split()
        storage = FileStorage()
        storage.reload()
        data = storage.all()
        d_all = []
        if not len(arg_split):
            for obj in data.values():
                d_all.append(obj.__str__())
        else:
            if arg_split[0] not in CLASS:
                print("** class doesn't exist **")
                return False
            for obj in data.values():
                if arg_split[0] == obj.__class__.__name__:
                    d_all.append(obj.__str__())
        print(d_all)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
