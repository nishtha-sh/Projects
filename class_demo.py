class Person:
    def __init__(self, name): #constructor
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
print(john.name)
john.talk()
