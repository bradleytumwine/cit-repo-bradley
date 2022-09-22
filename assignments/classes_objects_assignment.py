#Author: Tumwine Bradley
#QUESTIONS
#1. create a credit card class with the following attributes: card number, expiration date, and security code. 
# Create a method that will print out the card number, expiration date, and security code. 
# Create an instance of the class and call the method.

#2. create Animal class and Dog class. Make the Dog class inherit from the Animal class. 
# Add a bark method to the Dog class. Create an instance of the Dog class and call the bark method.

#3. create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. 
# The enqueue method should add an item to the queue. The dequeue method should remove an item from the queue. 
# The size method should return the size of the queue.

#4. create a class called Stack. The class should have the following methods: push, pop, and size. 
# The push method should add an item to the stack. The pop method should remove an item from the stack. 
# The size method should return the size of the stack.

#5. create a class called Person. The class should have the following attributes: name, age, and address. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working".

#6. create a class called Employee. The class should have the following attributes: name, age, and salary. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working". 
# Create a subclass of Employee called Programmer. 
# The Programmer class should have the following attributes: name, age, salary, and programming language. 
# The Programmer class should have the following methods: eat, sleep, work, and code. 
# The code method should print out the name of the person and the word "is coding in" and the programming language. 
# Create an instance of the Programmer class and call all the methods.

#7. create a class called Vehicle. The class should have the following attributes: make, model, and year. 
# The class should have the following methods: start, stop, and drive. 
# The start method should print out the make, model, and year of the vehicle and the word "is starting". 
# The stop method should print out the make, model, and year of the vehicle and the word "is stopping". 
# The drive method should print out the make, model, and year of the vehicle and the word "is driving". 
# Create a subclass of Vehicle called Car. 
# The Car class should have the following attributes: make, model, year, and color. 
# The Car class should have the following methods: start, stop, drive, and park. 
# The park method should print out the make, model, year, and color of the car and the word "is parking". 
# Create an instance of the Car class and call all the methods.

#8. create a class called Animal. The class should have the following attributes: name, color, and age. 
# The class should have the following methods: eat, sleep, and make_sound. 
# The eat method should print out the name of the animal and the word "is eating". 
# The sleep method should print out the name of the animal and the word "is sleeping".
# The make_sound method should print out the name of the animal and the word "is making a sound". 
# Create a subclass of Animal called Dog. 
# The Dog class should have the following attributes: name, color, age, and breed. 
# The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
# The bark method should print out the name of the dog and the word "is barking". 
# Create an instance of the Dog class and call all the methods.

#9. create a class of your choice. 
# It should have at least 3 attributes and 3 methods where one of the methods is a static method. 
# Implement polymorphism, encapsulation, and inheritance.

#SOLUTIONS
#1
from random import randint
class Credit_card:
    def _init_(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_card = security_code
    def cd (self):
        return self.card_number
    def exp(self):
        return self.expiration_date 
    def sc (self):
        return self.security_card

Bradley = Credit_card(randint(1000000000, 10000000000), "31/12/2030", randint(0000, 10000))
print(f"Card number :{Bradley.cd()} \n Expiry date:{Bradley.exp()} \n Security code: {Bradley.sc()}")

#2
class Animal:
    def _init_(self, name, type):
        self.name = name
        self.type = type
class Cat(Animal):
    def _init_(self, name, type):
        super()._init_(name, type)
    def purr(self):
        return "Meoow"
one = Cat("Bradley", "Garfield")
print(one.purr())

#3
class Queue:
    def _init_(self, element, lst, size):
        self.element = element
        self.lst = lst
        self.size = size
        
    def dequeue(self, element):
        if len(self.lst) != 0:
            self.lst.pop()
            return self.lst
        else:
            return 'The list is already empty'

    def length(self):
        return len(self.lst)

    def enqueue(self,element):
        if len(self.lst) != self.size:
            self.lst.insert(0,self.element)
            return self.lst
        else:
            return "list is full"