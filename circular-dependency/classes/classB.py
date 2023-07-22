from classes.classA import ClassA

class ClassB:
    def print_message(self):
        print("Hello World!")

    def use_dependency(self):
        print("Using dependency")
        ClassA().print_message()