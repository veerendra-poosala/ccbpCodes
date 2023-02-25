#SumOfNTermsInHarmonicSeries

n = int(input())

#series = 1 + 1/2 + 1/3 + 1/4 ---- 1/n 

harmonic_series = 0.0
for i in range(1,n+1):
    b = 1/i
    harmonic_series = b + harmonic_series
    #print("i",i,"harmonic_series",harmonic_series)
harmonic_series = round(harmonic_series,2)
print(harmonic_series)
    