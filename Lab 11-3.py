class Dog:
    species='mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def description(self):
        return '{} is {} years old'.format(self.name,self.age)
    def speak(self,sound):
        return '{} says {}'.format(self.name,sound)

class RusselTerrier(Dog):
    def run(self,speed):
        return '{} runs {}'.format(self.name,speed)

class Bulldog(Dog):
    def run(self,speed):
        return '{} runs {}'.format(self.name,speed)

thunder= Bulldog('Thunder',9)
print(thunder.description())
print(thunder.run('slowly'))

print(isinstance(thunder, Dog))

thunder_kid= Bulldog('Thunderkid',2)
print(isinstance(thunder,Dog))

kate= RusselTerrier('Kate',4)
print(isinstance(kate,Dog))
print('Thanks for understanding the concept of OOPs.')

#The reason of error was that thunder_kid was also a subclass of Dog. 
