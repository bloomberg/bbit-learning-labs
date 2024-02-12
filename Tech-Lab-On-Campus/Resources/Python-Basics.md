# Python Basics

### Creating a Class
Classes are the building blocks of object-oriented programming. In python, to create a class
we use the keyword `class` to define a class. For example, let's say I want to create a class called Animal. Within a class, there is a method called `__init__` which is an instance method that initalizes a newly created object.
Here is an example of a simple class:
```sh
class Animal:
    def __init__(self):
        pass
```

### Saving a Class Variable and Calling the Variable
In python, there is a keyword, `self`, which represents an instance of a class. This keyword allows you to access variables, methods, and attributes in the class. Let's build out our Animal class and pass in the name of an animal, and have a function named eat:
```sh
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
```
We can access the name initialized in the `__init__` method with `self`. When we want to create an object of this class with a name and call the method, `eat()`, it can access the name given and print out the statement. Remember, this is an example. You can initialize more variables within any of the class methods and access it through `self`!

### Inheritance
Inheritance allows us to define a class that can inherit methods and properties of another existing class. Let us use the example Animal class from above. Let's create a Dog class that inherits Animal:
```sh
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.animal_type = "dog"
```
Since `Dog` is inheriting `Animal`, we can use the method `eat()` on all `Dog` objects.
```sh
gigi = Dog("Gigi")
gigi.eat() # this will print: "Gigi is eating."
```

### Import Modules
To import a module, for example `sys`, use the keyword `import`:
```sh
import sys
```
If you are trying to import only one method or a class from another file / module:
```sh
from producer_interface import mqConsumerInterface
```

### Reading from Command Line Using sys
There are a few ways to read arguments from the command line, but we will go over using `sys`.
In this module, there is a variable, `sys.argv`, which is a list. Some things to note:

1. since sys.argv is a list, we can get the length of arguments with len()
2. sys.argv[0] will be the name of the file given
3. All arguments are **strings**!
