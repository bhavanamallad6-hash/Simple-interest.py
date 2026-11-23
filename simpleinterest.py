def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

si = simple_interest(p, r, t)

print("Principal amount:", p)
print("Rate of interest:", r)
print("Time:", t, "years")
print("Simple Interest:", si)