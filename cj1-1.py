# constants for ANSI color codes
GREEN   = "\033[92m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
RESET   = "\033[0m"


# main function
def main():
    # variables
    full_name = "Samik Pradhan"
    pronouns  = "he/him/his"
    fav_movie = "Interstellar"
    fav_food  = "ramen"

    # full message
    message = (
        f"Name: {GREEN}{full_name}{RESET}\n"
        + f"Pronouns: {MAGENTA}{pronouns}{RESET}\n"
        + f"My favorite movie is {CYAN}{fav_movie}{RESET}.\n"
        + f"My favorite food is {CYAN}{fav_food}{RESET}."
    )

    # print the message
    print(message)


# run the main function
if __name__ == "__main__":
    main()
