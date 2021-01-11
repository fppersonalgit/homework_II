

def fac_gen(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Enter number to know number factorial?\n"))
for c in fac_gen(n):
    print(c)