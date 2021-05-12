# Unix shell

Quick overview (more info [here](https://swcarpentry.github.io/shell-novice/))

1. Open a terminal:

    - Unix/Mac: search for an application called `Terminal`
    - Windows: search for `Git Bash`

2. in the terminal type:

```
$ cd <pystarters dir>
$ mkdir testRepo1
$ cd testRepo1
```

## Files 

1. create a text file using `nano`

```
$ nano myFirstScript.py
```

2. list content of the current directory directory: `ls`

```
$ ls
myFirstScript.py
```

3. copy a file: `cp` 

```
$ cp myFirstScript.py myNewScript.py
```

4. rename (move) a file: `mv`

```
$ mv myNewScript.py mySecondScript.py
```

5. delete a file: `rm`

```
rm mySecondScript.py
```

## Directories

1. print working directory: `pwd`

```
$ pwd
<pystarters dir>/testRepo1
```

2. create a directories: `mkdir`

```
$ mkdir code
$ ls
code  myFirstScript.py
```

3. rename (move) a directory: `mv`

```
$ mv code myCode
$ ls
myCode  myFirstScript.py
```

4. delete a directory: `rmdir` (the directory needs to be empty)

```
$ rmdir myCode
$ ls
myFirstScript.py
```

## Relative and absolute file/directory paths

If you are in the `scripts` directory you can refer to a file `x.csv` in the `data` directory using a relative or absolute file path:

**relative file path**
```
$ ls ../../data/x.csv
../../data/x.csv
```

**absolute file path**
```
$ ls <pystarters dir>/testRepo1/data/x.csv
<pystarters dir>/testRepo1/data/x.csv
```

## Exercises

1. create the following directory structure

```
<pystarters dir>
    testRepo1
        code
            src
            scripts
        data
        figures
        results
        doc
```

2. create data files

    - change to the `data` directory
    - create a file `x.csv` with five numbers of your choice, one number per row
    - create a file `y.csv` with five numbers of your choice, one number per row

3. move `myFirstScript.py` to the `scripts` directory

4. edit `myFirstScript.py` and add code for:

    - read `x.csv` and `y.csv` into variables `x` and `y` (for this you may want to use the function `genfromtxt` from the package `numpy`)
    - use the package `matplotlib` to plot `x` and `y`

5. execute `myFirstScript.py`
        
