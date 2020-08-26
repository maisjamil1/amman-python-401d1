import builtins

class Dog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"whoof from {self.name}"
    
    def __repr__(self):
        return self.name
    
    def __add__(self, other):
        return Dog(self.name + " and " + other.name)

    def __eq__(self, other):
        return self.name == other.name


if __name__ == '__main__':
    alex = Dog("Alex")
    oscar = Dog("Oscar")
    print(alex + oscar)
    print(alex == oscar)

