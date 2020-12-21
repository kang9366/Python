import statistics as st

a = [1, 2, 3, 4]

#평균
print(st.mean(a))
print(st.fmean(a)) #산술평균
print(st.geometric_mean(a)) #기하평균
print(st.harmonic_mean(a)) #조화평균

x = [i for i in range(100)]
print(st.median(x))
print(st.median_high(x))
print(st.median_low(x))
