class Dog:
    def __init__(self, name, age = 0, dog_type = '불명'):
        self.__name = name
        self.__age = age
        self.__dog_type = dog_type

    def name(self):
        return self.__name
    
    def dog_type(self):
        return self.__dog_type

    def age(self):
        return self.__age
    
    def speak(self):
        if self.__dog_type == '코코스파니엘':
            print("왈왈")
        elif self.dog_type == '골든리트리버':
            print("월월")
        else :
            print("멍멍")

class Cat(Dog):
    pass

cat1 = Cat("고양이")
print(cat1.name())