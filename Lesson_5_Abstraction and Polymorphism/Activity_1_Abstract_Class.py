from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print("Passed Vaue: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass")

class test_class(Absclass):
    def task(self):
        print("We are inside Test Class")

test_obj = test_class()
test_obj.task()
Abs_obj = Absclass()
Abs_obj.print(100)
test_obj.print(100)
