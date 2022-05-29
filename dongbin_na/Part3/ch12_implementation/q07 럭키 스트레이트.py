point = list(map(int,input()))
length = len(point)
half_idx = length // 2

a = point[:half_idx]
b = point[half_idx:]
if sum(a) == sum(b):
    print("LUCKY")
else:
    print("READY")