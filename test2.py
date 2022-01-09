# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 20:35:05 2014

@author: Rahul
"""

import numpy as np
import matplotlib.pyplot as plt

# print "new file"

a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])

c = a + b
d = np.sqrt(a/b)

plt.figure()
plt.plot(d)