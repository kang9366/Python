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

pp = [0.9, 0.95, 0.975, 0.99, 0.995]
print(norm.ppf(pp))

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("pdf, cdf of normal with data") # 전체 제목 설정
x = np.linspace(-3, 3, 100) #-3부터 3까지의 100개의 x에 대해 그림
rx.sort() #생성된 난수를 오름차순으로 정렬

ax1.plot(x, norm.pdf(x, loc=ave, scale=stdev), 'r-', lw = 2, alpha=0.6, label="norm pdf")
ax1.plot(x, norm().pdf(x), '-k', lw=2, label = "pdf from data")
ax1.hist(rx, density = True, histtype = 'stepfilled', alpha = 0.2)
ax1.legend(loc='best', frameon=False)

ax2.plot(x, norm.cdf(x, loc=ave, scale=stdev), 'r-', lw=2, alpha=0.6, label = 'norm cdf')
ax2.plot(x, norm().cdf(x), 'k-', lw=2, label = 'cdf from data')
ax2.hist(rx, density=True, histtype = 'stepfilled', alpha=0.2, cumulative=True, color = 'blue', edgecolor='red')
ax2.legend(loc='best', frameon=True)

plt.show()