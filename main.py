import variable_demo as vd


# not needed for video
def variables():
    print("1. variable types")
    print("2. type changes")
    print("/. exit")
    while True:
        user_in = input("please make a selection (1-9, /) : ")
        if user_in == '1':
            vd.variable_type_demo()
        elif user_in == '2':
            vd.type_change_demo()
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
