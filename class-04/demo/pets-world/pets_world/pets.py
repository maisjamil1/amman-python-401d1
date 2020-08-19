# Oscar = {
#     'name': 'Oscar D',
#     'age': 6 ,
#     'speak': 'Whooof'
# }

# Sherry = {
#     'name': 'Sherry R',
#     'age': 2,
#     'speak':'Meooow'
# }

# Alex = {
#     'name': 'Alex T',
#     'age': 5,
#     'speak': 'Whooof',
#     'greet': 'Hi my name is Alex'
# }


# Alex['password'] = 'password'


from abc import abstractmethod, ABC



class Pet(ABC): # ABC is the big class that any class can inherit from

    # Class Attribute
    count = 0

    def __init__(self, name):
        self.name = name
        # Refer to count using the class name since it's a class attribute
        Pet.count += 1

    # It's better to have __str__ for every sub class
    # def __str__(self):
    #     return f"Pet <{self.name}>"

    def __repr__(self):
        # This method will be called if we call the class instance from the command line
        return f" '{self.name}' "

    # speak is an abstract method because we want to force every sub class
    # to have a declaration for it
    @abstractmethod
    def speak(self):
        pass

    # A method without a decorator is by default an instance method
    def greet(self):
        return f"Hello, my name is {self.name}"

    # get__characteristics is a static mthodbecause it doesn't interact with
    # any attribute or methods in the class
    @staticmethod
    def get_characteristics():
        return "Likes to play with humans"

    # get_count is a class method because it works on the class level
    # we pass cls as a parameter to have access to attribues in class
    @classmethod
    def get_count(cls):
        return Pet.count


class Dog(Pet):
    def speak(self):
        return 'Whooof'
    def __str__(self):
        return f"Dog <{self.name}>"

class Cat(Pet):
    def __init__(self, name, nick_name):
        self.nick_name = nick_name # different that Dog class here
        # self.name = name => let's put this in the super class
        # super() refers to the super class
        # __ini__ is called manually to inistantiate Cat instances using Pet class __init__
        super().__init__(name)

    def __str__(self):
        return f"Cat <{self.name}>"

    def speak(self):
        return f'Meooow, my nick name is {self.nick_name}'
    def eat(self):
        return "Eating Cats Food"



if __name__=='__main__':
    oscar = Dog("Oscar D")
    print(oscar.greet())
    print(oscar.speak())
    sherry = Cat("Sherry R", "Shosho")
    print(sherry.greet())
    print(sherry.speak())
    print(f"Pets classes have this char.: {Pet.get_characteristics()}")
    print(Pet.get_count())
    print(oscar)
    oscar2 = Cat('Oscar D', 'Fake Cat')
    print(oscar2)

