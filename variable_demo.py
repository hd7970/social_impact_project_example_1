def variable_type():
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

def type_change():
    x = 7
    print("x = ", x, type(x))
    x = 7.0
    print("x = ", x, type(x))
    x = 'z'
    print("x = ", x, type(x))

def boolean_var():
    bt = True
    bf = False
    if bt == True and bf == False:
        print("All good boss!!")
    else:
        print("All is not well!!")
