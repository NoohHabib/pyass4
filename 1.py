import cmath

# read input for first complex number
a = complex(input("enter").strip())

# read input for second complex number
b = complex(input("enter").strip())

# addition of complex numbers
print("{:.2f} {:+.2f}i".format((a+b).real, (a+b).imag))

# subtraction of complex numbers
print("{:.2f} {:+.2f}i".format((a-b).real, (a-b).imag))

# multiplication of complex numbers
print("{:.2f} {:+.2f}i".format((a*b).real, (a*b).imag))

# division of complex numbers
print("{:.2f} {:+.2f}i".format((a/b).real, (a/b).imag))

# modulus of first complex number
print("{:.2f}".format(abs(a)))

# modulus of second complex number
print("{:.2f}".format(abs(b)))