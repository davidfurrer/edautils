# eda-utils
helper functions for exploratory data analysis (EDA)

----
docs can be found at:
https://davidfurrer.github.io/edautils/

-----

## Example usage

```python
import edautils

edautils.plot_numerical(df, num_cols = 5, target_col = 'diagnosis')
```

![Numerical Features](png/numerical_example2.png)


```python
edautils.plot_numerical(df, num_cols = 5)
```


![Numerical Features](png/numerical_example1.png)