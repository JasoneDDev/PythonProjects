import random
import re
#fizz buzz

#  divisible by 3 print fizz divisible by 5 print buzz if both print fizz buzz

for num in range(100):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)


# fibonacci sequence

a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b

# fibonacci generator


def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        yield a
        a, b = b, a + b


for item in fib(10):
    print(item)



#lists
my_list = [10, 23, 12, 5, 20, 8]

my_dict = {'name': 'city', 'degrees': '2', 'numbers': 'go up'}

my_set = {2, 4, 5, 7, 2, 5, 1, 2, 7, 6, 3, 5, 67}

my_tuple = ([2, 4], ['bob', 45], 45, 'sam')

for i in my_list:
    print(i)

for i in my_set:
    print(i)

for key, val in my_dict.items():
    print('my {} is {}'.format(key, val))

for i in my_tuple:
    print(i)


# list comprehensions

my_list = [1, 2, 3, 4, 6, 7, 8, 8, 8, 9, 9, 4, 3, 22, 21]

# each number in list squared

squares = [num * num for num in my_list]

print(squares)

# randomize my list

random.shuffle(my_list)
print(my_list)


class tester(object):
    def __init__(self, name):
        self.name = name
        self.catname = ''

    def reveal_name(self):
        print('my name is {}'.format(self.name))

    def extraSecretName(self, cat):
        print("and my cat's name is {}".format(cat))


class superHero(tester):
    def __init__(self, name, hero_name, catname):
        super(superHero, self).__init__(name)
        self.hero_name = hero_name
        self.catname = catname

    def reveal_name(self):
        super(superHero, self).reveal_name()
        super(superHero, self).extraSecretName(self.catname)
        print('...and I am {}'.format(self.hero_name))


jason = tester('Jason')
jason.reveal_name()

Ivy = superHero('Ivy', 'Batman', 'catchuly')
Ivy.reveal_name()