# Python Basics

## Import Modules
To import a module, for example `sys`, use the keyword `import`:
```sh
import sys
```
If you are trying to import only one method or a class from another file / module:
```sh
from dog_interface import DogInterface
```

## Creating a Class
Classes are the building blocks of object-oriented programming. In python, to create a class
we use the keyword `class` to define a class. For example, let's say I want to create a class called Animal. Within a class, there is a constructor method called `__init__` which initalizes a newly created object.
Here is an example of a simple class:
```sh
class Animal:
    def __init__(self, name):
        # body of constructor
        self.name = name

    def eat(self):
        print(self.name, "is eating.")
```

## Saving a Instance Variable and Calling the Variable
In python, there is a keyword, `self`, which represents an instance of a class. This keyword allows you to access variables, methods, and attributes in the class. Let's build out our Dog interface and pass in the name of a dog, and have a function named bark:
```sh
class Dog(DogInterface):
    def __init__(self, name) -> None:
        # Save parameters to instance variable
        self.name = name

    def bark(self) -> None:
        # Print {name of dog} is barking!
        print(self.name, "is barking!")
```
We can access the name initialized in the `__init__` method with `self`. When we want to create an object of this class with a name and call the method, `bark()`, it can access the name given and print out the statement. Remember, this is an example. You can initialize more variables within any of the class methods and access it through `self`!

## Creating an Interface
Python does not have a keyword for interfaces. An interface is an abstract class that defines methods which are not implemented. An interface is implemented in the same way as a class, however, an interface will have abstract methods so you will see the keyword `pass` in those methods. That means that any subclass will construct those methods how it wants to use them. So two different classes which inherit from the same intergace will inherit the same functions, but can have different implementations.
Here is an example of a simple interface:
```sh
class DogInterface:
    def __init__(self, name) -> None:
        # Save parameters to class variables
        pass

    def bark(self) -> None:
        # Print {name of dog} is barking!
        pass
```

## Inheritance
Inheritance allows us to define a class that can inherit methods and properties of another existing class or interface. Let us use the example DogInterface from above. Let's create a Dog class that inherits DogInterface:
```sh
class Dog(DogInterface):
    def __init__(self, name):
        # Save parameters to instance variable
        self.name = name

    def bark(self):
        # Print {name of dog} is barking!
        print(self.name, "is barking!")
```
Since `Dog` is inheriting `DogInterface`, we implement the methods according to how we want both methods to work.

To inherit from another class would have the same initialization, but the child class can have different methods. Let's write a Dog class inheriting the class Animal that was mentioned in the Creating a Class section:
```sh
class Dog(Animal):
    def __init__(self, name):
    self.name = name
```
Since `Dog` is inheriting `Animal`, we can use the method `eat()` on all `Dog` objects.
```sh
snoopy = Dog("Snoopy")
snoopy.eat() # this will print: "Snoopy is eating."
```

## Reading from Command Line Using sys
There are a few ways to read arguments from the command line, but we will go over using `sys`.
In this module, there is a variable, `sys.argv`, which is a list. Some things to note:

1. since sys.argv is a list, we can get the length of arguments with len()
2. sys.argv[0] will be the name of the file given
3. All arguments are **strings**!

**Example**

Command:
```sh
python3 read_cmd_line.py apple banana
```
Code:
```sh
"""
Read arguments from command line using sys.argv
"""

import sys

print("Name of the program using sys.argv[0]: ", sys.argv[0])
print("Length of arguments given including program name: ", len(sys.argv))
print("Argument list: ", sys.argv)
print("Argument list type: ", type(sys.argv))
print("Give the first argument (after program name): ", sys.argv[1])
```
Output:
![alt text](../images/sys-argv-image.jpg)
