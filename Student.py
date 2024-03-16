from Person import Person

class Student(Person):

    def __init__(self, name, age, curs, grupa):
        super().__init__(name, age)
        self.__curs = curs
        self.__grupa = grupa

    @property
    def curs(self): return self.__curs

    @curs.setter
    def curs(self, curs): self.__curs = curs

    @property
    def grupa(self): return self.grupa

    @grupa.setter
    def grupa(self, grupa): self.grupa = grupa

    def get_info(self):
        print(f"name: {self.name} ||age: {self.age} ||curs: {self.__curs} ||grupa: {self.__grupa}")
        

