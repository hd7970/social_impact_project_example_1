import variable_demo as vd
import conditional_demo as cd

# not needed for video
def variables():
    while True:
        print("1. variable types")
        print("2. type changes")
        print("/. exit")
        user_in = input("please make a selection (0-9) : ")
        if user_in == '1':
            vd.variable_type()
            print("\n")
        elif user_in == '2':
            vd.type_change()
            print("\n")
        elif user_in == '3':
            vd.boolean_var()
            print("\n")
        elif user_in == '0':
            print("\n")
            return
        else:
            exit(0)


def conditionals():
    while True:
        print("1. variable types")
        print("")
        print("/. exit")

# This does not need to be shown in the video.  This is more so for making sure my code works, and is usable.
def main():
    while True:
        print("1. variable demos")
        print("2. ")
        print("0. exit")
        user_in = input("please make a selection (0-9) : ")
        if user_in == '1':
            variables()
        elif user_in == '0':
            exit(0)
        else:
            exit(1)

#if exit
#   return
#write_menu

# This single function call is what allows the program to run.
main()
