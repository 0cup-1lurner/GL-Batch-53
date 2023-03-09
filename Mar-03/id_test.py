
g = 9000
h = 9000

print(id(g))
print(id(h))
print(g is h)

g += 1
h += 1

print("aft",id(g))
print("aft",id(h))
print("aft", g is h)
