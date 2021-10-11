#!/usr/bin/python3
""" inherits_from module"""


def inherits_from(obj, a_class):
    """function to verifie subclass"""
    if issubclass(type(obj), a_class) and not isinstance(obj, a_class):
        return True
    else:
        return False
