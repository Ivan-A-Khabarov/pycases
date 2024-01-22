a = 3
b = 5
def f(a:int, b:int):
    if b == 0:
        return 1
    return f(a,b-1) * a

print(f(a, b))