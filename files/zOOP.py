class Pet:
    def __init__(self, name, species, age, gender):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__gender = gender

    def get_info(self):
        print(f"Имя: {self.__name}, Вид: {self.__species}, Возраст: {self.__age}, Пол: {self.__gender}")

class Dog(Pet):
    def __init__(self, name, age, gender, breed):
        super().__init__(name, "Собака", age, gender)
        self.__breed = breed

    def bark(self):
        print("Гав!")

class Cat(Pet):
    def __init__(self, name, age, gender, color):
        super().__init__(name, "Кошка", age, gender)
        self.__color = color

    def meow(self):
        print("Мяу!")

dog = Dog("Рекс", 3, "Мужской", "Лабрадор")
cat = Cat("Мурка", 2, "Женский", "Рыжий")
dog.get_info()
cat.get_info()
dog.bark()
cat.meow()
pets = [dog, cat]
for pet in pets:
    pet.get_info()