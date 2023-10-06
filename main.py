import problems


def load_problem(n):
    match n:
        case 1:
            problems.one()
        case _:
            raise ValueError()

def main():
    print("Hello Joseph! \n")
    print("It is great that you are working on the programming problem once again.")

    while True:
        try:
            problem_number = int(input("Please select the number of the program you would like to run: "))
            load_problem(problem_number)
            break
        except ValueError:
            print("Input is not a number or problem number is not found. Please try again.")


if __name__ == "__main__":
    main()
