# function that asks user to provide a float
def get_float() -> float:
    # loop until valid input received
    while True:
        # get user input
        user_input = input("Enter a float: ")

        # test input to see if it is valid
        try:
            fl = float(user_input)
            break
        except:
            print("Invalid input! Try again.")

    # return user input as a float
    return fl


# function that asks user to provide an int
def get_int() -> int:
    # loop until valid input received
    while True:
        # get user input
        user_input = input("Enter an integer: ")

        # test input to see if it is valid
        try:
            i = int(user_input)
            break
        except:
            print("Invalid input! Try again.")

    # return user input as an int
    return i


# main function
def main():
    # 2 floats for addition
    fl1 = get_float()  # 2.34
    fl2 = get_float()  # 5.6364

    # print output
    print(
        f"Sum of two floating point numbers:\t\t\t{fl1} + {fl2} = {fl1 + fl2}\n"
        + f"\t\t\t\t\t\t\ttype({fl1 + fl2}):\t{type(fl1 + fl2)}"
    )

    # 2 integers for subtraction
    i1 = get_int()  # 7
    i2 = get_int()  # 4

    # print output
    print(
        f"Difference between two integers:\t\t\t{i1} - {i2} = {i1 - i2}\n"
        + f"\t\t\t\t\t\t\ttype({i1 - i2}):\t{type(i1 - i2)}"
    )

    # 1 float and 1 integer for multiplication
    fl3 = get_float()  # 3.9812
    i3 = get_int()  # 8

    # print output
    print(
        f"Product of a floating point number and an integer:\t{fl3} * {i3} = {fl3 * i3}\n"
        + f"\t\t\t\t\t\t\ttype({fl3 * i3}):\t{type(fl3 * i3)}"
    )


# call the main function
if __name__ == "__main__":
    main()
