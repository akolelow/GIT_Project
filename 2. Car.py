n = int(input())
m = int(input())
count_pereriv = (n - 1) // m
time = count_pereriv * ((1 + count_pereriv) // 2)
print(n + time)
