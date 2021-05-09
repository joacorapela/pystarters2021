# Functions

## Function declaration and invokation

# Function declaration
def make_a_sound():
    print("quack")

# Function invokation
make_a_sound()

## Functions can return values

def agree():
    return True

if agree():
    print("Splendid")
else:
    print("That was unexpected")

## Functions can receive one argument

def echo(aString):
    return aString + " " + aString

print(echo("Pystarters"))

## Functions can receive multiple arguments

def greet(firstName, lastName, msg):
    print("Hello", firstName + ' ' + lastName + ', ' + msg)

greet("Monica", "Garcia", "Good morning!")

## Functions can be documented

def greet(firstName, lastName, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", firstName + ' ' + lastName + ', ' + msg)

## and we can read this function documentation

help(greet)

## or any other function documentation

help(print)

## Functions can have default arguments

def greet(firstName, lastName, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", firstName + ' ' + lastName + ', ' + msg)

greet("Ann", "Robinson")
greet("Bruce", "Knight", "How do you do?")

## Non-default arguments cannot follow default arguments in function definitions

def greet(msg="Good morning!", firstName, lastName):
    """
    This function greets to
    the person with the
    provided message.

    If message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", firstName + ' ' + lastName + ', ' + msg)

