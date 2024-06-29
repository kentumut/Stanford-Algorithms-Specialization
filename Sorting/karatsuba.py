def karatsuba(X, Y):
    # Base case for recursion
    if X < 10 or Y < 10:
        return X * Y

    # Calculate the size of the numbers
    n = max(len(str(X)), len(str(Y)))
    m = n // 2

    # Split the digit sequences in the middle
    X_1, X_0 = divmod(X, 10**m)
    Y_1, Y_0 = divmod(Y, 10**m)

    # Recursively calculate three products
    z_0 = karatsuba(X_0, Y_0)
    z_2 = karatsuba(X_1, Y_1)
    z_1 = karatsuba(X_1 + X_0, Y_1 + Y_0) - z_2 - z_0

    # Combine the results
    return z_2 * 10**(2*m) + z_1 * 10**m + z_0

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(f'Result: {karatsuba(x,y)}')
