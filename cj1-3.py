"""What I learned:
I learned how to create functions. I also learned how to call functions.
"""


# function that cubes a value and adds 8 to that result
def f(x):
    return (x * x * x) + 8


# main function
def main():
    # variable to call the function f(x) on
    x = 9

    # calling the f(x) function on the specified variable
    result = f(x)

    # printing the result of the function
    print(result)

    # if statement to print "YAY!" if the result is >27
    if result > 27:
        print("YAY!")


# call the main function
if __name__ == "__main__":
    main()
