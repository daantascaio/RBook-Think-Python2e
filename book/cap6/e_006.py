def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result


# factorial(20)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square


x = 1
y = x + 1
print(c(x, y+3, x+y))
