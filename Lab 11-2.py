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

spinter= Bulldog('spinter',12)
print(spinter.description())
print(spinter.run('fast'))

roger= RusselTerrier('Roger',5)
print(spinter.description())
print(spinter.run('quickly'))
