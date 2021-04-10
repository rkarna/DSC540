"""## Assignment: Week3&4 Assignment\n",
  "## Name: Karna, RajasekharReddy\n",
  "## Date: 04/10/2021"""
import pandas as pd
import numpy as np
sa = pd.Series([7.3,-2.5,3.4,1.5],index = ['a','c','d','e'])
print("Original Data Series-A:")
print(sa)
sb = pd.Series([-2.1,3.6,-1.5,4,3.1],index = ['a','c','e','f','g'])
print("Original Data Series-B:")
print(sb)
add_s = sa + sb
print("Adding Series-A and Series-B:")
print(add_s)
sub_s = sb - sa
print("Substract Series-A from Series-B:")
print(sub_s)