class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and my sex is {self.gender}.")

person2 = Person("JaredOkoth", 25, "male")
person2.introduce()
