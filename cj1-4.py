# Pangolin class
class Pangolin:
    # initializer function
    def __init__(
        self,
        arm_len: float,
        leg_len: float,
        num_eyes: int,
        has_tail: bool,
        is_furry: bool,
    ) -> None:
        self.arm_length = arm_len
        self.leg_length = leg_len
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    # member function that prints the data of the object
    def print_data(self) -> None:
        print(
            "The physical characteristics of this animal are as follows:\n"
            + f"\tLength of arms:\t{self.arm_length}\n"
            + f"\tLength of legs:\t{self.leg_length}\n"
            + f"\tNumber of eyes:\t{self.num_eyes}\n"
            + f"\tHas a tail?\t{'Yes' if self.has_tail else 'No'}\n"
            + f"\tIs furry?\t{'Yes' if self.is_furry else 'No'}"
        )


# testing
if __name__ == "__main__":
    bob = Pangolin(3.4, 2.2, 3, True, False)

    bob.print_data()
