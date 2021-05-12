# Functions

## Setup

1. open a terminal
2. type `conda activate pystarters`
3. open the Python interpreter by typing `python` in ther terminal


## Function declaration and invokation

### Function declaration
```
def make_a_sound():
    print("quack")
```

### Function invokation
```
make_a_sound()
```

## Functions can return values

```
def agree():
    return True

if agree():
    print("Splendid")
else:
    print("That was unexpected")
```

## Functions can receive one argument

```
def echo(aString):
    return aString + " " + aString

print(echo("Pystarters"))
```

## Functions can receive multiple arguments

```
def greet(firstName, lastName, msg):
    print("Hello", firstName + ' ' + lastName + ', ' + msg)

greet("Monica", "Garcia", "Good morning!")
```

## Functions can be documented

```
def greet(firstName, lastName, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", firstName + ' ' + lastName + ', ' + msg)
```

### and we can read this function documentation

```
help(greet)
```

### or any other function documentation

```
help(print)
```

## Functions can have default arguments

```
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
```

## Non-default arguments cannot follow default arguments in function definitions

```
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
```

## Exercises

1. create a function `plot_1D_data(x, y)` in script `doMyFirstScript.py` to plot `y` as a function of `x`.

2. call this function using `x` and `y` from `x.csv` and `y.csv`.

3. add parameters `xlabel`, `ylabel`, `title`, `line_color`, and `line_type` with default values

4. invoke `plot_1D_data` with default and non-default arguments.

