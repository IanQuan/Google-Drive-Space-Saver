import math

d = 1e-10
if math.isclose(d, 0, abs_tol=1e-9):
    result = "One root"
else:
    result = "Two root"

print(result)
