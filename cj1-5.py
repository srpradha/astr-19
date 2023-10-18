import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.io import ascii

# constant that defines number of rows in table
NUM_ROWS = 1000


# main function
def main():
    # generate 1000 x vals from 0 to 2pi
    x_vals = np.linspace(0, 2 * np.pi, num=NUM_ROWS)

    # calculate the sin of each of the values above
    sin_x_vals = np.sin(x_vals)

    # creating a table
    data = Table([x_vals, sin_x_vals], names=["x", "sin(x)"])

    # name of file to write the table into
    fname = "data.txt"

    # write table to file
    ascii.write(data, fname, format="commented_header")

    # read data into variable
    data_in = ascii.read(fname)

    # print formatted table
    print(data_in)

    print(f"\nNOTE: full table can be found in {fname}")

    # EXTRA: graph for fun

    # plot the table
    plt.plot(x_vals, sin_x_vals, label=r"$y = \sin(x)$")
    # title of plot
    plt.title(r"Graph of $x$ vs $\sin(x)$")
    # legend
    plt.legend(loc=1, framealpha=0.95)
    # show the plot
    plt.show()


if __name__ == "__main__":
    main()
