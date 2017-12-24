#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy
import os
import random
import statistics


board = [None] * 100
board[1] = 38
board[4] = 14
board[9] = 31
board[16] = 6
board[21] = 42
board[28] = 84
board[36] = 44
board[48] = 26
board[49] = 11
board[51] = 67
board[56] = 53
board[62] = 19
board[64] = 60
board[71] = 91
board[80] = 100
board[87] = 24
board[93] = 73
board[95] = 75
board[98] = 78

trials = 100000
results = [0] * trials

for i in range(trials):
    pos = 0
    moves = 0

    while pos < 100:
        moves = moves + 1
        pos = board[pos] or pos   # chute or latter from previous move
        pos = pos + random.randint(1, 6)

    results[i] = moves

results = sorted(results)

percentile_bins = [0, 25, 50, 75, 99, 99.9, 100]
percentiles = numpy.percentile(results, [0, 25, 50, 75, 99, 99.9, 100])

stats = [
    ('count', trials),
    ('mean', statistics.mean(results)),
    ('stdev', statistics.stdev(results)),
    ('mode', statistics.mode(results)),
]
for name, val in stats:
    print("%10s: %10.2f" % (name, val))

for ix in range(len(percentile_bins)):
    print("%8.1fth: %10.2f" % (percentile_bins[ix], percentiles[ix]))

try:
    os.mkdir('data')
except FileExistsError:
    pass

plt.style.use('seaborn-white')
plt.figure(figsize=(16, 9), dpi=144)
plt.title('Chutes and Ladders Turns-to-Complete Histogram')
plt.xlabel('Turns')
plt.ylabel('Rate')
plt.hist(results, bins=50, normed=True)
plt.style.use('seaborn-white')
plt.savefig(
    'data/chutes_and_ladders_histogram.png',
    format='png',
    bbox_inches='tight',
)
