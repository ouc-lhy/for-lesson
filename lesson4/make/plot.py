#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=argparse.FileType('r'))
parser.add_argument('-o')
args = parser.parse_args()

data = np.loadtxt(args.i)
plt.plot(data[:, 0], data[:, 1], 'bo-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2')
plt.grid(True)
plt.savefig(args.o)
