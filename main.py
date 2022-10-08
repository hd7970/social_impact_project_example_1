import variable_demo as vd


# not needed for video
def variables():

    while True:
        print("1. variable types")
        print("2. type changes")
        print("/. exit")
        user_in = input("please make a selection (1-9, /) : ")
        if user_in == '1':
            vd.variable_type_demo()
            print("\n")
        elif user_in == '2':
            vd.type_change_demo()
            print("\n")
        elif user_in == '3':
            vd.boolean_demo()
            print("\n")
        elif user_in == '/':
            print("\n")
            return
        else:
            exit(1)

# This does not need to be shown in the video.  This is more so for making sure my code works, and is usable.
def main():
    while True:
        print("A. variable demos")
        print("/. exit")
        user_in = input("please make a selection (A-Z, /) : ")
        if user_in == 'A' or 'a':
            print(" ")
            variables()
        elif user_in == '0':
            exit(0)
        else:
            exit(1)


# This single function call is what allows the program to run.
main()
