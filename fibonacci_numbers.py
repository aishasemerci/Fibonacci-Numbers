# -*- coding: utf-8 -*-
"""FIBONACCI NUMBERS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IRCEhunTp2lcsfLDdXrXC45KM4cAYdHM
"""

fibonacci_num = []
count = 0
for i in list(range(10)):
  count += 1
  if count <= 2:
    fibonacci_num.append(1)
  else:
    fibonacci_num.append(fibonacci_num[i-1] + fibonacci_num[i-2]) 

print("Fibonacci Numbers:", fibonacci_num)