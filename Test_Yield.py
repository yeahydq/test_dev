def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        c=b
        yield c
        #print b
        a, b = b, a + b
        n = n + 1

a=fab(5)
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
