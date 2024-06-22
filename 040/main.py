f = []
i = 1

while(len(f) <= 1000000):
    str_i = str(i)
    for s in str_i:
        f.append(int(s))
    i += 1

print(f"fraction 1: {f[0]}")
print(f"fraction 10: {f[9]}")
print(f"fraction 100: {f[99]}")
print(f"fraction 1000: {f[999]}")
print(f"fraction 10000: {f[9999]}")
print(f"fraction 100000: {f[99999]}")
print(f"fraction 1000000: {f[999999]}")

result = f[0]*f[9]*f[99]*f[999]*f[9999]*f[99999]*f[999999]
print(result)