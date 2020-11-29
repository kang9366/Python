from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import statistics

#정규분포 난수 발생
rx = norm.rvs(size=100)
ave = statistics.mean(rx)
#표본 표준편차
stdev = statistics.stdev(rx)
print(ave, stdev)
