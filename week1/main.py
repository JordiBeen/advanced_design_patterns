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
print('We have a dog named:')
print(dog1.GetName())
print('We have a dog named:')
print(dog2.GetName())
print('We have a bird named:')
print(bird.GetName())
print('We have a snake named:')
print(snake.GetName())

# Let our animals make some sounds
print('They make the following sounds:')
dog1.MakeSound()
dog2.MakeSound()
bird.MakeSound()
