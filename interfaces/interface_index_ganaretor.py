"""This finds a new 'register_number' for a book from the Book's db."""
import uuid

from project.apps import register_key


def generate_register_numbers():
    """
    TODO: This finds a new 'register_number' for the Book's db.
         This ('_number') is a new number (string type). We will be check\
          and if is it unique, we ('_number') to saving in tuple (set())
        If it is not unique , returns the re-start this function.
        We want to find/create the book's unique number.
    :param register_number: set()/tuple.
    :return: [_number, generate_register_numbers(register_key)]
    """
    
    set_numbers = []
    status = True
    
    while status:
        _number = uuid.uuid4()
        # CHECK LENGTH 'set_numbers' if > 0
        if str(_number) in set_numbers:
            # RESTART the FUNCTION
            continue
        if register_key.isdisjoint(str(_number)):
            register_key.add(str(_number))
            status = False
            return str(_number)
        
        if not register_key.isdisjoint(str(_number)):
            set_numbers.append(str(_number))
        
            