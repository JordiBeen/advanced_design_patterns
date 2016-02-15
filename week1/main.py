from classes.Dog import Dog
from classes.Bird import Bird
from classes.Snake import Snake

# Create a new dog
dog1 = Dog()

# Create a second dog
dog2 = Dog()

# Create a bird
bird = Bird()

# Create a snake
snake = Snake()

_animals = []
_animals.append(dog1)
_animals.append(dog2)
_animals.append(bird)
_animals.append(snake)

# Set names for all our new animals
dog1.SetName('Boris')
dog2.SetName('Jaap')
bird.SetName('Tweety')
snake.SetName('Samuel')

# Let some animals eat and move
print('Letting some animals eat and move:')
dog1.Eat()
bird.Eat()
snake.Move()
dog2.Move()

# Lets get the names of our animals
print('We have an animal called:')
for animal in _animals:
    if hasattr(animal, 'GetName'):
        animal.GetName()
    else:
        print('This animal doesn\'t have a name')

# Let our animals make some sounds
print('They make the following sounds:')
for animal in _animals:
    if hasattr(animal, 'MakeSound'):
        animal.MakeSound()
    else:
        print('This animal doesn\'t make sound')
