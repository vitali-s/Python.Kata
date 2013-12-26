def incrementor(n):
    return lambda x: x + n

def lambda_1():
    expression = lambda x: x * 2;

    expression(expression(2))

print incrementor(5)(6)