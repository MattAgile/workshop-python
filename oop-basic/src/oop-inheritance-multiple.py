class Male:
    gender = 'male'


class Gieroj:
    status = 'hero'


class Astronaut(Male, Gieroj):
    def __init__(self, name):
        self.name = name

    def say_hallo(self):
        print(f'My name... {self.name}')


ivan = Gieroj(name='Иван Иванович')
ivan.say_hallo()        # My name... Иван Иванович
ivan.status             # hero
ivan.gender             # male
