from classes.classB import ClassB


class ClassA:
    def print_message(self):
        print("Hello World!")

    def use_dependency(self):
        print("Using dependency")
        ClassB().print_message()