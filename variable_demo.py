def variable_type_demo():
    i = 10  # integer
    f = 1.1  # floating point
    c = 'H'  # character (python makes it a string)
    s = "hello there"  # string

    print("i = ", i)
    print("the type is : ", type(i))
    print("f = ", f)
    print("the type is : ", type(f))
    print("c = ", c)
    print("the type is : ", type(c))
    print("s = ", s)
    print("the type is : ", type(s))

def type_change_demo():
    x = 7
    print("x = ", x, type(x))
    x = 7.0
    print("x = ", x, type(x))
    x = 'z'
    print("x = ", x, type(x))