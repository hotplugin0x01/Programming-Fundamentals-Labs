class Dog:
    species='mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def discription(self):
        return '{} is {} years old'.format(self.name,self.age)
    def speak(self,sound):
        return '{} says {}'.format(self.name,sound)

razer=Dog('Razer',6)
print(razer.discription())
print(razer.speak('woof woof'))
