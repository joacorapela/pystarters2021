# 1_unixShell.md

## Excercise 2

3. File `myFirstScript.py`

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("../../data/x.csv")
y = np.genfromtxt("../../data/y.csv")

plt.plot(x, y)
plt.show()

plt.savefig("../../figures/1_exercise2.png")
```
