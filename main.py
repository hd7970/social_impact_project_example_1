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

    # if i == 10:
    #     print("yep that sure is a 10")
    #
    # # potential discussion about how python does the guess work for var type
    # if i == 10.0:
    #     print("yep that sure is a 10.0")
    # else:
    #     print("in what world is that 10.0")


def type_change_demo():
    x = 7
    print("x = ", x, type(x))
    x = 7.0
    print("x = ", x, type(x))
    x = 'z'
    print("x = ", x, type(x))


# not needed for video
def variables():
    print("1. variable types")
    print("2. type changes")
    print("/. exit")
    while True:
        user_in = input("please make a selection (1-9, /) : ")
        if user_in == '1':
            variable_type_demo()
        elif user_in == '2':
            type_change_demo()
        elif user_in == '/':
            exit(0)
        else:
            exit(1)

# This does not need to be shown in the video.  This is more so for making sure my code works, and is usable.
def main():
    print("A. variable demos")
    print("/. exit")
    while True:
        user_in = input("please make a selection (A-Z, /) : ")
        if user_in == 'A' or 'a':
            variables()
        elif user_in == '/':
            exit(0)
        else:
            exit(1)


# This single function call is what allows the program to run.
main()
