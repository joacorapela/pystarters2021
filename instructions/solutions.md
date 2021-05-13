# 1_unixShell.md

## Excercise 2

File `myFirstScript.py`

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("../../data/x.csv")
y = np.genfromtxt("../../data/y.csv")

plt.plot(x, y)
plt.show()
```
![1exercise2](figures/1_exercise2.png)

# 3_functions.md

## Excercise 1

File `myFirstScript.py`

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_1D_data(x, y, xlabel="x", ylabel="y", title="My First Plot",
                 line_color="red", line_style="dotted"):
    plt.plot(x, y, color=line_color, linestyle=line_style)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

x = np.genfromtxt("../../data/x.csv")
y = np.genfromtxt("../../data/y.csv")

plot_1D_data(x, y)
plt.show()

plot_1D_data(x, y, xlabel="data", ylabel="predictions",
             title="Plot with custom parameters", line_color="blue",
             line_style="dashed")
plt.show()
```
Default parameters:
![3_exercise1_default](figures/3_exercise1_default_params.png)

Custom parameters:
![3_exercise1_custom](figures/3_exercise1_custom_params.png)

