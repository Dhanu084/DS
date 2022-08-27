from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):

    @abstractmethod
    def walk():
        pass

class Leapord(Animal):
    def walk(self):
        print('Leapord Walks')

l= Leapord()
l.walk()