# pip install tabulate

'''
* printing small tables without hassle: just one function call, formatting is guided by the data itself

* authoring tabular data for lightweight plain-text markup: multiple output formats suitable for further editing or transformation

* readable presentation of mixed textual and numeric data: smart column alignment, configurable number formatting, alignment by a decimal point
'''

from tabulate import tabulate

table = [["Sun", 696000, 1989100000], ["Earth", 6371, 5973.6], ["Moon", 1737, 73.5], ["Mars", 3390, 641.85]]

A = tabulate(table)

print(A)

'''
OutPut:
-----  ------  -------------
Sun    696000     1.9891e+09
Earth    6371  5973.6
Moon     1737    73.5
Mars     3390   641.85
-----  ------  -------------
'''

