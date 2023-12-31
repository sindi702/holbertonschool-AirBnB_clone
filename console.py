#!/usr/bin/python3
'''Module of AirBNB console'''
import cmd
import sys
import os
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''console func'''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''Exit the program with EOF'''
        return True

    def emptyline(self):
        ''' dont execute empty line entered'''
        pass

    def do_create(self, arg):
        '''create new instance'''
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg not in ls:
            print("** class doesn't exist **")
            return False
        new = eval(arg)()
        storage.save()
        print(new.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance'''
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in ls:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        for key, value in storage.all().items():
            if value.id == arg[1]:
                if value.__class__.__name__ == arg[0]:
                    print(value)
                    return
                print('** no instance found **')

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name'''
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in ls:
            print("** class doesn't exist **")
            return False
        if len(arg) != 2:
            print("** instance id missing **")
            return False
        check = arg[0] + '.' + arg[1]
        if check in storage.all().keys():
            del storage.all()[check]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, arg):
        '''Prints all str repr of instance of said Class'''
        if len(arg) != 0:
            if arg not in ls:
                print("** class doesn't exist **")
                return False
            for key, value in storage.all().items():
                if value.__class__.__name__ == arg:
                    print(value)
        else:
            for key, value in storage.all().items():
                print(value)

    def do_update(self, arg):
        '''update an instance based in the class name'''
        arg = arg.split()
        var = 0
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in ls:
            print(arg)
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        for key, value in storage.all().items():
            if value.id == (arg[1]):
                val = arg[3].split('"')
                if len(val) > 1:
                    setattr(value, arg[2], val[1])
                    storage.save()
                    var += 1
        if var == 0:
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            print(" ** value missing **")
            return False


if __name__ == '__main__':
    ls = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
    HBNBCommand().cmdloop()
