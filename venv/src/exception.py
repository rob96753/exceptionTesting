#! /usr/bin/python3

class myException(Exception):
     def __init__(self, location, value):
            self.value = value
            self.location = location
     def __str__(self):
            return f'Exception in {self.location} was {self.value}'


try:
    raise myException('main', 'custom exception')
except myException as e:
    print(e)
