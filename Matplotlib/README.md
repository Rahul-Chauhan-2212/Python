# Matplotlib

## What is Matplotlib?
Matplotlib is a **data visualization library** in Python used to create graphs, charts and plots from structured or numeric data.  
It works very well with NumPy, Pandas and Seaborn.

---

## Installation

```bash
pip install matplotlib

```

---

## Basic Usage Structure

```python
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x, y)
plt.show()
```

## Common Plot Types
| Plot Type    | Function        |
| ------------ | --------------- |
| Line Plot    | `plt.plot()`    |
| Bar Chart    | `plt.bar()`     |
| Scatter Plot | `plt.scatter()` |
| Pie Chart    | `plt.pie()`     |
| Histogram    | `plt.hist()`    |


## Figure & Label Styling
```python
plt.title("Sales Growth")
plt.xlabel("Month")
plt.ylabel("Revenue")
```

## Saving Plots
```python
plt.savefig("output.png")
```

## Why Matplotlib Matters?

* Base library (foundation for Seaborn)
* Highly customizable
* Interview friendly
* Used widely in data science & analytics
