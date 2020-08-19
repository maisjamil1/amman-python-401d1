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



class Pet(ABC):

    count = 0

    def __init__(self, name):
        self.name = name
        Pet.count += 1

    # def __str__(self):
    #     return f"Pet <{self.name}>"

    def __repr__(self):
        return f" '{self.name}' "

    @abstractmethod
    def speak(self):
        pass

    def greet(self):
        return f"Hello, my name is {self.name}"

    @staticmethod
    def get_characteristics():
        return "Likes to play with humans"

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
        self.nick_name = nick_name
        # self.name = name
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

